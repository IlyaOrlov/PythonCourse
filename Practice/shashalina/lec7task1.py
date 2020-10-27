# Написать функцию для подсчета количества рабочих дней между двумя датами (даты передаются в качестве параметров)
import datetime
from datetime import timedelta

def workDays(startYear, startMonth, startDay, endYear, endMonth, endDay):
    startDate = datetime.date(startYear, startMonth, startDay)
    endDate = datetime.date(endYear, endMonth, endDay)
    numOfDays = (endDate - startDate)
    date = startDate
    workDays = 0

    for d in range((numOfDays.days)+1):
        if datetime.date.weekday(date) != 5 and datetime.date.weekday(date) != 6:
            workDays += 1
        date += timedelta(days=1)
    print('Number of workDays: {}'.format(workDays))
    return workDays

workDays(2020, 9, 11, 2020, 9, 27)
