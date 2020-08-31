import datetime


def working_days(first_data, second_data):
    delta = second_data - first_data     # - object timedelta
    return delta.days - delta.days//7*2


if __name__ == "__main__":
    print(working_days(datetime.datetime(2020, 8, 21), datetime.datetime(2020, 12, 31)))
    print(f"We have {working_days(datetime.datetime.now(), datetime.datetime(2020, 12, 31))} working days in 2020")
