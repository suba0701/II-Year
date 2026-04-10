from datetime import date

year = 2028

try:
    date(year, 2, 29)
    print(True)   # 2028 is a leap year
except ValueError:
    print(False)
