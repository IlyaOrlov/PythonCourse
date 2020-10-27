from _datetime import datetime,date

date1 = input('Ввведите дату начала в формате гггг мм дд:')
date1 = date1.split(' ')
date1 = date(int(date1[0]), int(date1[1]), int(date1[2]))

date2 = input('Ввведите дату окончания в формате гггг мм дд:')
date2 = date2.split(' ')
date2 = date(int(date2[0]), int(date2[1]), int(date2[2]))

difference = ((date2 - date1).days)
weekday = datetime.weekday(date1)
working_day = []
for i in range(difference + 1):
    if weekday < 5:
        working_day.append(weekday)
        weekday += 1
    elif weekday > 5:
        weekday = 0
    else:
        weekday += 1
print('Количесво рабочих денй за период ' + str(len(working_day)))