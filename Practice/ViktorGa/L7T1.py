import datetime


def working_days(first_data, second_data):
    delta = second_data - first_data
    first_day = first_data.weekday()

    if first_day == "Saturday":
        return (delta.days+1) - (delta.days+1)//7*2 - 2
    elif first_day == "Sunday":
        return (delta.days + 1) - (delta.days + 1) // 7 * 2 - 1

    return (delta.days+1) - (delta.days+1)//7*2


if __name__ == "__main__":
    print(working_days(datetime.datetime(2020, 2, 14), datetime.datetime(2020, 2, 20)))
