from collections import defaultdict
from datetime import datetime

dates = [
    "2026-03-10",
    "2026-03-11",
    "2026-03-14",
    "2026-03-17",
    "2026-03-18",
]

groups = defaultdict(list)
for s in dates:
    dt = datetime.strptime(s, "%Y-%m-%d").date()
    weekday_name = dt.strftime("%A")       
    groups[weekday_name].append(dt)
for weekday in sorted(groups):
    print(f"{weekday} → {len(groups[weekday])} dates")
