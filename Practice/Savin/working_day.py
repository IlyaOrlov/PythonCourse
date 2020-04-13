from datetime import datetime
from datetime import timedelta

first_date = '10-04-2020'
last_date = '30-04-2020'

def working_day(first_date, last_date):
    fdate = datetime.strptime(first_date, '%d-%m-%Y')
    ldate = datetime.strptime(last_date, '%d-%m-%Y')
    delta = ldate - fdate
    date = fdate
    work_day = 0
    for i in range(int(delta.days)+1):
        if date.strftime('%A') != 'Saturday' and date.strftime('%A') != 'Sunday':
            work_day += 1
        date += timedelta(days=1)
    return work_day
print(working_day(first_date, last_date))


