import datetime

sundays = 0
for year in range(2022, 2023):
    for month in range(1, 13):
        d = datetime.date(year, month, 1)
        if d.weekday() == 6:
            print(year)
            print(month)
            sundays = sundays + 1

print(sundays)
