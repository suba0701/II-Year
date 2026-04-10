from datetime import date, timedelta

today = date.today()
for i in range(5):
    day = today + timedelta(days=i)
    print(day.isoformat())
