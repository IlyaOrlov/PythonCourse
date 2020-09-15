import datetime


def workdays_count(date_start, date_end):
    if date_start >= date_end:
        return 0
    current_date = date_start
    count = 0
    while current_date <= date_end:
        if is_week_day(current_date):
            count += 1
        current_date = current_date + datetime.timedelta(days=1)
    return count


def is_week_day(date):
    if date.weekday() == 5 or date.weekday() == 6:
        return False
    return True


date1 = datetime.datetime.now()
date2 = date1+datetime.timedelta(days=30)
print(workdays_count(date1, date2))
