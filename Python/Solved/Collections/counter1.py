from collections import Counter
from datetime import datetime

logins = [
    "2026-03-10 10:00",
    "2026-03-10 10:15",
    "2026-03-10 10:45",
    "2026-03-10 11:30",
    "2026-03-11 09:30",
    "2026-03-11 11:45",
    "2026-03-11 14:00"
]

# parse timestamps and collect hours (0-23)
hours = [datetime.strptime(ts, "%Y-%m-%d %H:%M").hour for ts in logins]

counts = Counter(hours)

# most common hour and its count
if counts:
    hour, cnt = counts.most_common(1)[0]
    # convert hour to human-friendly "10 AM / 3 PM" format
    suffix = "AM" if hour < 12 else "PM"
    display_hour = hour if 1 <= hour <= 12 else (12 if hour % 12 == 0 else hour % 12)
    print(f"{display_hour} {suffix} → {cnt} logins")
else:
    print("No logins")
