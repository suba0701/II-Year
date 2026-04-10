from datetime import date

# current date
today = date.today()

# format: day-number - FullMonthName - Year  WeekdayName
print(today.strftime("%d-%B-%Y %A"))
