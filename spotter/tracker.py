"""Post mentees' GitHub activity to Slack.

`python tracker.py daily`  : channel reminder to commit, and DM anyone with no commits in 3 days.
`python tracker.py weekly` : per-mentee summary of the last 7 days.
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
        lines.append(f"• {mention(m)}: {n} commits, active {min(len(days), 7)}/7 days. Top repos: {repos or 'private'}")
    unknown = [m["github"] for m, c in results if c is None]
    if unknown:
        lines.append(f":warning: GitHub user not found: {', '.join(unknown)}")
    return "\n".join(lines)


def post(channel, text):
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        json.dumps({"channel": channel, "text": text}).encode(),
        {"Authorization": f"Bearer {os.environ['SLACK_BOT_TOKEN']}", "Content-Type": "application/json; charset=utf-8"},
    )
    with urllib.request.urlopen(req) as r:
        resp = json.load(r)
    if not resp["ok"]:  # Slack returns HTTP 200 even on errors
        raise SystemExit(f"Slack error: {resp['error']}")


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "daily"
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
