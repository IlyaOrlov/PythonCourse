import datetime

def day_works(date1, date2):
    date = date1
    work_day = 0

    while date <= date2:
        if date.weekday() < 5:
            work_day += 1
        date += datetime.timedelta(days=1)
    return work_day


if __name__ == "__main__":
    date1 = datetime.datetime(2020, 10, 5)
    date2 = datetime.datetime(2020, 10, 16)
    print(day_works(date1, date2))