import datetime

def day_works(date1, date2):
    delta = date1 - date2
    date = date1
    work_day = 0

    for i in range(int(delta.days) + 1):
        if date.weekday() < 5:
            work_day += 1
        date += datetime.timedelta(days=1)
    return work_day

if __name__ == "__main__":
    date1 = datetime.datetime(2020, 10, 15)
    date2 = datetime.datetime(2020, 10, 1)
    print(day_works(date1, date2))