from datetime import date, timedelta

d = date(2026, 3, 10)

# last day of previous month
prev_month_last_day = d.replace(day=1) - timedelta(days=1)

try:
    # try to set same day in previous month
    prev_same_day = prev_month_last_day.replace(day=d.day)
except ValueError:
    # fallback (shouldn't be needed for 10th of month, but safe for e.g. 31st -> 30/29/28)
    prev_same_day = prev_month_last_day

print(prev_same_day)  # 2026-02-10
