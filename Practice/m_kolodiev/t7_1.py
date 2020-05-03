from datetime import datetime, timedelta
import time


def work_days(start, end):
    delta = timedelta(days=1)
    diff = 0
    while start != end:
        if start.weekday() < 5:
            diff += 1
        start += delta
    return diff


start_date = datetime(2020, 4, 1)
end_date = datetime(2020, 4, 20)
print(work_days(start_date, end_date))
