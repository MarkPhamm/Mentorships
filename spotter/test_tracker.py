from datetime import datetime

import json
import os

from tracker import mention, roster_message, to_nudge, weekly_message


def contrib(n, repos=(), days=()):
    return {
        "totalCommitContributions": n,
        "restrictedContributionsCount": 0,
        "commitContributionsByRepository": [
            {"repository": {"nameWithOwner": r}, "contributions": {"totalCount": k}} for r, k in repos
        ],
        "contributionCalendar": {"weeks": [{"contributionDays": [{"date": d, "contributionCount": 1} for d in days]}]},
    }


a = {"github": "a", "slack": "U1"}
b = {"github": "b", "slack": "U2"}
c = {"github": "ghost", "slack": "U3"}

# daily
assert to_nudge([(a, contrib(3)), (b, contrib(0)), (c, None)]) == [b]

# weekly
since, until = datetime(2026, 10, 29), datetime(2026, 11, 5)
msg = weekly_message(
    [(b, contrib(0)), (a, contrib(5, [("a/x", 4), ("a/y", 1)], ["2026-10-28", "2026-10-30", "2026-11-01"])), (c, None)],
    since,
    until,
)
assert msg.index("<@U1>") < msg.index("<@U2>"), "sorted by commits"
assert "5 commits, active 2/7 days" in msg, "day before window ignored"
assert "a/x (4), a/y (1)" in msg
assert "<@U2>: :x: 0 commits" in msg
assert ":white_check_mark:" in msg, "commits get a green check"
assert ":white_check_mark:" not in msg.split("<@U2>")[1], "zero commits keep the x, not a check"
assert "not found: ghost" in msg

# mentee with a GitHub handle but no Slack ID still shows up, by name
d = {"name": "Mia Tran", "github": "mia", "slack": None}
msg = weekly_message([(d, contrib(4, [("mia/x", 4)], ["2026-11-02"]))], since, until)
assert "• Mia Tran: :white_check_mark: 4 commits, active 1/7 days. Top repos: mia/x (4)" in msg

# a single commit reads "1 commit", not "1 commits"
msg = weekly_message([(a, contrib(1, [("a/x", 1)], ["2026-11-01"]))], since, until)
assert ":white_check_mark: 1 commit, active" in msg
assert "1 commits" not in msg

# a DM channel ID is a valid DM target but not a mentionable member ID
dm = {"name": "Mia Tran", "github": "mia", "slack": "D0CF7S9JS4A"}
assert mention(dm) == "Mia Tran"
assert mention({"name": "A", "slack": "U1"}) == "<@U1>"

# roster table: header row, one row per mentee, GitHub and LinkedIn as links
roster = [
    {"name": "Gwen Nguyen", "github": "gwenniehub", "linkedin": "https://www.linkedin.com/in/gwennienguyen/"},
    {"name": "No Links", "github": None, "linkedin": None},
]
text, blocks = roster_message(roster)
table = blocks[1]
assert table["type"] == "table"
assert [c["text"] for c in table["rows"][0]] == ["Name", "GitHub", "LinkedIn"], "first row is the header"
assert all(len(row) == 3 for row in table["rows"]), "every row has three cells"
assert table["rows"][1][1]["elements"][0]["elements"][0]["url"] == "https://github.com/gwenniehub"
assert table["rows"][1][2]["elements"][0]["elements"][0]["text"] == "in/gwennienguyen"
assert table["rows"][2][1] == {"type": "raw_text", "text": "—"}, "missing links render as a dash"
assert text == "Mentee roster: 2 mentees"

# the real roster gets exactly one row each
with open(os.path.join(os.path.dirname(__file__), "mentees.json")) as f:
    real = json.load(f)
assert len(roster_message(real)[1][1]["rows"]) == len(real) + 1

print("ok")
