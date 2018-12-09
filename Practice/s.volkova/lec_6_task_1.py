#for Python 3.6
#Lecture 6 task 1
'''Программа не учитывает праздничные выходные дни'''

from datetime import date, timedelta


def basic_counter(date1, date2):
    '''Функция принимает две даты и рассчитывает число рабочих дней между ними,
    при этом первая из дат включается в промежуток, вторая - нет.'''
    dayslist = []
    d = date1
    #Составляет список из дней недели (в виде номеров от 1 до 7),
    #которые попали в промежуток между нужными датами
    while d != date2:
        dayslist.append(d.isoweekday())
        d += timedelta(days=1)
    #Рассчитывает по списку дней недели количество рабочих дней в промежутке
    key_days = {1:1, 2:1, 3:1, 4:1, 5:1, 6:0, 7:0}
    working_days = 0
    for i in dayslist:
        working_days += key_days[i]
    return working_days

def workdays_counter(date1, date2):
    '''Функция принимает две даты и рассчитывает число рабочих дней между ними
    при этом первая из дат включается в промежуток, вторая - нет.
    Способ расчета меняется в зависимости от того, какое число дней получено.'''
    days_diff = date2 - date1
    #Для периода короче семи дней
    if days_diff.days < 7:
        return basic_counter(date1, date2)
    #Для периода, кратного семи
    elif days_diff.days % 7 == 0:
        return (days_diff.days // 7) * 5
    #Для периода больше недели и некратного семи
    else:
        interm_date = date1 + timedelta(weeks = days_diff.days // 7)
        return (days_diff.days // 7) * 5 + basic_counter(interm_date, date2)
def main(date1, date2):
    print('''Число дней в промежутке между {} и {}: {}, из них рабочих: {}'''.format(
           date1.isoformat(), date2.isoformat(), (date2 - date1).days,
           workdays_counter(date1, date2)))

if __name__ == '__main__':
    main(date(2019, 1, 25), date(2019, 1, 28))
    main(date(2018, 12, 11), date(2018, 12, 27))
    main(date(2019, 1, 30), date(2019, 2, 20))
    main(date(2016, 1, 1), date(2017, 1, 1))



  


