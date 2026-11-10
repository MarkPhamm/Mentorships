"""Post mentees' GitHub activity to Slack.

`python tracker.py daily`  : channel reminder to commit, and DM anyone with no commits in 3 days.
`python tracker.py weekly` : per-mentee summary of the last 7 days.
`python tracker.py roster` : the mentees.json roster as a table in the channel.

Roster posts are skipped (and the payload printed) when SLACK_BOT_TOKEN is unset, so it's a dry run.
"""
import json
import os
import sys
import urllib.request
from datetime import datetime, timedelta, timezone

QUERY = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      totalCommitContributions
      restrictedContributionsCount
      commitContributionsByRepository(maxRepositories: 3) {
        repository { nameWithOwner }
        contributions { totalCount }
      }
      contributionCalendar {
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}
"""


def fetch(login, since, until, token):
    """GitHub contributions for `login` in the window, or None if the user doesn't exist."""
    body = {"query": QUERY, "variables": {"login": login, "from": since.isoformat(), "to": until.isoformat()}}
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        json.dumps(body).encode(),
        {"Authorization": f"bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as r:
        user = json.load(r)["data"]["user"]
    return user and user["contributionsCollection"]


def commits(c):
    # restricted = private-repo contributions, only visible if the mentee enabled it on their profile
    return c["totalCommitContributions"] + c["restrictedContributionsCount"]


# One per day, rotating, so the reminder doesn't turn into wallpaper.
DAILY_REMINDERS = [
    "Commit today. The market is congested and nobody is coming to save you. "
    "Your GitHub is the only proof you've got.",
    "Ten comfortable reps never got anyone in shape. One small commit, every day. Push it.",
    "The kid who gets your internship is committing tonight. Are you?",
    "If you slept 8 hours and had time for TikTok, you're not burnt out. Commit something.",
    "Recruiters don't read promises, they read green squares. Prove, don't beg. Push today.",
    "Everyone says they're learning SQL. Your commits are what make you not a minion.",
    "No commit, no proof. No proof, no interview. Push something before you sleep.",
    "There's no \"weekends\" when you don't achieve what you want. "
    "Saturday is just another day. Commit something.",
]
NUDGE = (
    "3 days, 0 commits. That's how people end up graduating with no internship and a dead GitHub. "
    "Push something tonight, even one line. Consistency beats talent you don't show."
)


def to_nudge(results):
    """Mentees with zero commits in the window. Unknown GitHub users (None) are skipped."""
    return [m for m, c in results if c and not commits(c)]


def mention(m):
    """Slack @-mention, or the roster name when there's no ID or it's not a member ID (D/C/G).

    A DM channel ID still works as a DM target, but Slack won't resolve it inside `<@...>`.
    """
    sid = m.get("slack") or ""
    return f"<@{sid}>" if sid.startswith(("U", "W")) else m["name"]


def weekly_message(results, since, until):
    lines = [f"*Weekly GitHub summary* ({since:%b %d} to {until:%b %d})"]
    found = [(m, c) for m, c in results if c]
    for m, c in sorted(found, key=lambda mc: -commits(mc[1])):
        n = commits(c)
        if not n:
            lines.append(f"• {mention(m)}: :x: 0 commits this week")
            continue
        days = {
            d["date"]
            for w in c["contributionCalendar"]["weeks"]
            for d in w["contributionDays"]
            if d["contributionCount"] and d["date"] >= f"{since:%Y-%m-%d}"
        }
        repos = ", ".join(
            f"{r['repository']['nameWithOwner']} ({r['contributions']['totalCount']})"
            for r in c["commitContributionsByRepository"]
        )
        lines.append(f"• {mention(m)}: :white_check_mark: {n} commit{'' if n == 1 else 's'}, active {min(len(days), 7)}/7 days. Top repos: {repos or 'private'}")
    unknown = [m["github"] for m, c in results if c is None]
    if unknown:
        lines.append(f":warning: GitHub user not found: {', '.join(unknown)}")
    return "\n".join(lines)


def _plain(text):
    return {"type": "raw_text", "text": text}


def _link(label, url):
    # Table cells render mrkdwn only through rich_text, so build the link by hand.
    return {
        "type": "rich_text",
        "elements": [
            {"type": "rich_text_section", "elements": [{"type": "link", "url": url, "text": label}]},
        ],
    }


def roster_message(mentees):
    """`text` plus Block Kit `blocks` showing the roster as a native Slack table.

    Columns are name, GitHub and LinkedIn. The header row is the first row of the table.
    """
    rows = [[_plain("Name"), _plain("GitHub"), _plain("LinkedIn")]]
    for m in mentees:
        name = m.get("name") or m.get("github") or "—"
        gh = m.get("github")
        li = m.get("linkedin")
        display = li.split("linkedin.com/in/")[-1].rstrip("/") if li else None
        rows.append(
            [
                _plain(name),
                _link(gh, f"https://github.com/{gh}") if gh else _plain("—"),
                _link(f"in/{display}", li) if li else _plain("—"),
            ]
        )
    blocks = [
        {"type": "section", "text": {"type": "mrkdwn", "text": f"*Mentee roster*: {len(mentees)} mentees"}},
        {"type": "table", "column_settings": [{"is_wrapped": True}] * 3, "rows": rows},
    ]
    return f"Mentee roster: {len(mentees)} mentees", blocks


def post(channel, text, blocks=None):
    payload = {"channel": channel, "text": text}
    if blocks:
        payload["blocks"] = blocks
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        json.dumps(payload).encode(),
        {"Authorization": f"Bearer {os.environ['SLACK_BOT_TOKEN']}", "Content-Type": "application/json; charset=utf-8"},
    )
    with urllib.request.urlopen(req) as r:
        resp = json.load(r)
    if not resp["ok"]:  # Slack returns HTTP 200 even on errors
        raise SystemExit(f"Slack error: {resp['error']}")


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "daily"
    if mode == "roster":
        with open(os.path.join(os.path.dirname(__file__), "mentees.json")) as f:
            mentees = json.load(f)
        text, blocks = roster_message(mentees)
        payload = json.dumps({"channel": os.environ.get("SLACK_CHANNEL", "#all-mentee"), "text": text, "blocks": blocks}, indent=2)
        if not os.environ.get("SLACK_BOT_TOKEN"):
            print(payload)
            print("\n(dry run: SLACK_BOT_TOKEN not set, nothing posted)")
            return
        post(os.environ["SLACK_CHANNEL"], text, blocks)
        print(text)
        return

    with open(os.path.join(os.path.dirname(__file__), "mentees.json")) as f:
        # Slack is only needed to DM someone; a missing ID still gets them into the weekly summary.
        mentees = [m for m in json.load(f) if m.get("github")]
    until = datetime.now(timezone.utc)
    since = until - timedelta(days=7 if mode == "weekly" else 3)
    token = os.environ["GITHUB_TOKEN"]
    results = [(m, fetch(m["github"], since, until, token)) for m in mentees]

    if mode == "weekly":
        text = weekly_message(results, since, until)
        print(text)
        post(os.environ["SLACK_CHANNEL"], text)
        return

    post(os.environ["SLACK_CHANNEL"], DAILY_REMINDERS[until.toordinal() % len(DAILY_REMINDERS)])
    for m in to_nudge(results):
        if not m.get("slack"):
            print(f"no Slack ID for {m['github']}, skipping nudge")
            continue
        print(f"nudging {m['github']} via {m['slack']}")
        try:
            post(m["slack"], NUDGE)  # a user ID (or a DM channel ID) = DM from the app
        except (Exception, SystemExit) as e:
            print(f"nudge to {m['github']} failed: {e}")  # one bad channel shouldn't stop the rest


if __name__ == "__main__":
    main()
