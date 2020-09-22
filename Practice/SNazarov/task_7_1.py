import datetime



def day_works(new_date, next_date):

    delta = new_date - next_date
    date = new_date
    working_days = 0

    for i in range(int(delta.days) + 1):
        if date.weekday() < 5:
            working_days += 1
        date += datetime.timedelta(days=1)

    return working_days

if __name__ == "__main__":

    first_date = datetime.datetime(2020, 9, 16)
    second_date = datetime.datetime(2020, 9, 1)
    print(day_works(first_date, second_date))