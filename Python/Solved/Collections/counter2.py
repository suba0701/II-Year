from collections import Counter
from datetime import datetime

events = [
    "2025-01-10",
    "2025-01-20",
    "2025-02-05",
    "2025-02-15",
    "2025-03-01"
]

# Parse and normalize to "YYYY-MM" keys
months = [datetime.strptime(d, "%Y-%m-%d").strftime("%Y-%m") for d in events]
counts = Counter(months)

# Print counts in chronological order
for month in sorted(counts):
    print(f"{month}: {counts[month]}")
