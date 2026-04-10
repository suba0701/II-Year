from collections import Counter
from datetime import datetime

logins = [
    "2026-03-10 10:00",
    "2026-03-10 12:00",
    "2026-03-11 09:30",
    "2026-03-11 11:45",
    "2026-03-11 14:00"
]

# parse timestamps and collect dates (as date objects or ISO strings)
dates = [datetime.strptime(ts, "%Y-%m-%d %H:%M").date() for ts in logins]

counts = Counter(dates)

# Print counts in a predictable order
for day in sorted(counts):
    print(f"{day.isoformat()}: {counts[day]}")
