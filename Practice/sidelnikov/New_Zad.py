import datetime

def workday(date1, date2):
    sum = 1
    res = (date1 + datetime.timedelta(x) for x in range((date1 - date2).days + 1))
    for day in res:
        if day.weekday() < 5:
            sum += 1
    return sum
date1 = datetime.date(2020, 4, 11)
date2 = datetime.date(2020, 4, 2)
print(workday(date1, date2))