from datetime import date, timedelta

def count_sundays(year: int, month: int) -> int:
    # start at the first day of the month
    d = date(year, month, 1)
    # move to the next month and back one day to get last day
    if month == 12:
        next_month = date(year + 1, 1, 1)
    else:
        next_month = date(year, month + 1, 1)
    last_day = next_month - timedelta(days=1)

    cnt = 0
    while d <= last_day:
        if d.weekday() == 6:   # Sunday
            cnt += 1
        d += timedelta(days=1)
    return cnt

print(count_sundays(2025, 1))  # 4
