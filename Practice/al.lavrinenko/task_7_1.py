import datetime as dt


def num_of_working_days(start_date, end_date):
    if start_date > end_date:
        print("Error: start date cannot be greater than end date")
        return None
    total_num_of_days = (end_date - start_date).days + 1
    num_of_whole_weeks = total_num_of_days // 7
    counter = num_of_whole_weeks * 5

    # Добавляем оставшиеся рабочие дни, которые не попали в целые недели
    for i in range(num_of_whole_weeks*7, total_num_of_days):
        weekday = (start_date + dt.timedelta(i)).weekday()
        if weekday != 5 and weekday != 6:
            counter += 1
    return counter


a = dt.date(2010, 4, 3)
b = dt.date(2020, 4, 9)
print(num_of_working_days(a, b))
a = dt.date(2020, 4, 1)
b = dt.date(2020, 4, 11)
print(num_of_working_days(a, b))
