from _datetime import datetime, timedelta


def workDay(date1, date2):
    # exclude the possibility of errors caused by the input format

    if (date1.find('.') != -1):
        time1 = date1.split(".")
    else:
        time1 = date1.split("-")
    if (date2.find('.') != -1):
        time2 = date2.split(".")
    else:
        time2 = date2.split("-")

    month1 = time1[1]
    month2 = time2[1]

    if (len(time1[0]) == 4):
        year1 = time1[0]
        day1 = time1[2]
    else:
        day1 = time1[0]
        year1 = time1[2]

    if (len(time2[0]) == 4):
        year2 = time2[0]
        day2 = time2[2]
    else:
        day2 = time2[0]
        year2 = time2[2]

    # get dates from processed arguments
    currnt_day = datetime(int(year1), int(month1), int(day1))
    next_day = datetime(int(year2), int(month2), int(day2))

    # create generator and get difference between dates
    if (next_day>currnt_day):
        daygen = (currnt_day + timedelta(x + 1) for x in range((next_day - currnt_day).days))
    else:
        daygen = (next_day + timedelta(x + 1) for x in range((currnt_day - next_day).days))

    count_day = 0
    for i in daygen:
        if i.weekday() < 5:
            count_day += 1
    print(f"Количество рабочих дней составило {count_day}")


workDay("14.09.2020", "21.09.2020")
workDay("21.09.2020", "14.09.2020")
workDay("14-09-2020", "2020-09-21")
