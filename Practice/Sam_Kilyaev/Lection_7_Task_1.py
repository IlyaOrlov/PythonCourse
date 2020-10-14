import datetime
import sys

first_date = ''
second_date = ''


def work_day(year1, mounth1, day1, year2, mounth2, day2):
    d1 = datetime.date(year1, mounth1, day1)
    d2 = datetime.date(year2, mounth2, day2)
    daygenerator = (d1 + datetime.timedelta(x + 1) for x in range((d2 - d1).days))
    return sum(1 for day in daygenerator if day.weekday() < 5)


def reformat_dates(first_date, second_date):
    count = 0
    a = first_date.split('.')
    print(a)
    b = second_date.split('.')
    print(b)
    year1 = ''
    mounth1 = ''
    day1 = ''
    year2 = ''
    mounth2 = ''
    day2 = ''
    for i in a:
        count += 1
        print(i)
        if count == 1:
            year1 = int(i)
            print(year1)
        elif count == 2:
            mounth1 = int(i)
            print(mounth1)
        elif count == 3:
            day1 = int(i)
            print(day1)
    count = 0
    for j in b:
        print(j)
        count += 1
        if count == 1:
            year2 = int(j)
        elif count == 2:
            mounth2 = int(j)
        elif count == 3:
            day2 = int(j)
    print(year1, mounth1, day1, year2, mounth2, day2)
    return work_day(year1, mounth1, day1, year2, mounth2, day2)


# Запуск программы через: Lection_7_Task_1.py [param1/2019.12.5] [param2/2019.12.30]
if __name__ == '__main__':
    count = 0
    for param in sys.argv:
        if count == 1:
            first_date = param  # 2019.12.5
        elif count == 2:
            second_date = param  # 2019.12.30
        elif count >= 3:
            print('Extra Date')
        count += 1

result = reformat_dates(first_date, second_date)
print(f'Work day between {first_date} and {second_date} is {result}')
