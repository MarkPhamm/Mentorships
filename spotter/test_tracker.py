from datetime import datetime

from tracker import to_nudge, weekly_message


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
assert "not found: ghost" in msg
print("ok")
