from datetime import date,timedelta

d1 = date(2020, 4, 1)
d2 = date(2020, 5, 1)

def work_days(d1, d2):
    date = d1
    work_days = 0 # задаем счетчик для кол-ва рабочих дней
    while date <= d2:  # пока date  от d1 до d2
        if date.weekday() != 5 and date.weekday() != 6:# если date  не равен 5 и 6
            work_days += 1  # увеличиваем счетчик
        date += timedelta(days=1)  # увеличиваем date по дням


    return work_days

print(work_days(d1,d2))