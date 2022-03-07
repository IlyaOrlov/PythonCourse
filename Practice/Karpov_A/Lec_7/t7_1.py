from datetime import datetime
from datetime import timedelta

start_date = '01-08-2020'
end_date = '10-09-2020'

def working_day(statr_date, end_date):
    fd = datetime.strptime(start_date, '%d-%m-%Y')
    ld = datetime.strptime(end_date, '%d-%m-%Y')
    zoom = ld - fd
    date = fd
    work_days = 0
    for i in range(int(zoom.days)+1):
        if date.strftime('%A') != 'Saturday' and date.strftime('%A') != 'Sunday':
            work_days += 1
        date += timedelta(days=1)
    return work_days
print(working_day(start_date, end_date))