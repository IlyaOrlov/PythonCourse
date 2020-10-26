import datetime


def working_days(first_data, second_data):
    count = 0
    current_day = first_data
    while current_day <= second_data:
        if current_day.weekday() < 5:
            count += 1
        current_day = current_day + datetime.timedelta(days=1)
    return count


print(working_days(datetime.datetime(2020, 10, 2), datetime.datetime(2020, 10, 10)))
