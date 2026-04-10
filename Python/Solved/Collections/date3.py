from datetime import date

d = date(2026, 3, 10)
iso_year, iso_week, iso_weekday = d.isocalendar()
print(iso_week)  # 11
