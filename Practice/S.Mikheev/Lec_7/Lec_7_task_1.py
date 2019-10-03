from datetime import datetime, date, timedelta


def date_range(date1, date2, step=1):
    date1 = datetime.date(datetime.strptime(date1, '%d.%m.%Y'))
    date2 = datetime.date(datetime.strptime(date2, '%d.%m.%Y'))
    if step > 0:
        if date1 < date2:
            a = date1
            while date1 < date2:
                yield a
                a = date1 + timedelta(step)
                date1 += timedelta(step)
        else:
            return 'Error!!!'
    elif step < 0:
        if date1 < date2:
            a = date1
            while date1 > date2:
                yield a
                a = date1 + timedelta(step)
                date1 += timedelta(step)

    elif step == 0:
        return 'Error, step = 0!'


def count_day(date1, date2):
    count = 0
    for single_date in date_range(date1, date2):  # не включая date2
        if single_date.weekday() != 5 and single_date.weekday() != 6:
            count += 1
        else:
            continue
    return count


d1 = '02.09.2019'
d2 = '15.12.2019'
print('Число рабочих дней на интервале от {} до {}: {}'.format(d1, d2, count_day(d1, d2)))
