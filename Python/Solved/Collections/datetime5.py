from datetime import date

d = date(2026, 3, 14)

# weekday(): Monday=0, ..., Sunday=6
if d.weekday() >= 5:           # 5 = Saturday, 6 = Sunday
    print("Weekend")
else:
    print("Weekday")
