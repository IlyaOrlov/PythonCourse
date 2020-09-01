import datetime


def working_days(first_data, second_data):
    delta = second_data - first_data                             # - object timedelta
    first_day = first_data.strftime("%A")                        # - day of week

    if first_day == "Saturday":
        return (delta.days+1) - (delta.days+1)//7*2 - 2          # for start at Saturday ' - 2 day'
    elif first_day == "Sunday":
        return (delta.days + 1) - (delta.days + 1) // 7 * 2 - 1  # for start at Sunday   ' - 1 day'

    return (delta.days+1) - (delta.days+1)//7*2


if __name__ == "__main__":
    print(working_days(datetime.datetime(2020, 8, 24), datetime.datetime(2020, 8, 30)))
    print(working_days(datetime.datetime(2020, 8, 31), datetime.datetime(2020, 9, 13)))
    print(working_days(datetime.datetime(2020, 9, 12), datetime.datetime(2020, 9, 16)))
    print(working_days(datetime.datetime(2020, 9, 13), datetime.datetime(2020, 9, 16)))
    print(working_days(datetime.datetime(2020, 9, 21), datetime.datetime(2020, 9, 23)))
    print(f"We have {working_days(datetime.datetime.now(), datetime.datetime(2020, 12, 31))} working days in 2020")
    
