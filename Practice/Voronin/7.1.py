from _datetime import datetime,date
d1 = input('Введите дату в формате ГГГГ,М,Д :')
d1 = d1.split(',')
d1 = date(int(d1[0]), int(d1[1]), int(d1[2]))
d2 = input('Введите дату в формате ГГГГ,М,Д :')
d2 = d2.split(',')
d2 = date(int(d2[0]), int(d2[1]), int(d2[2]))
q_day = ((d2 - d1).days)
d1w = datetime.weekday(d1)
work_day = []
for i in range(q_day + 1):
    if d1w < 7:
        if 0 < d1w < 6:
            work_day.append(d1w)
            d1w += 1
        else:
            d1w += 1
    else:
        d1w = 0

print('Количество рабочих дней ' + str(len(work_day)))


