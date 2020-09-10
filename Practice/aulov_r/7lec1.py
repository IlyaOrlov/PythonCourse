from _datetime import datetime,date

a = input('Entered date гггг,мм,дд :')
a = a.split(',')
a = date(int(a[0]), int(a[1]), int(a[2]))
b = input('Entered date гггг,мм,дд :')
b = b.split(',')
b = date(int(b[0]), int(b[1]), int(b[2]))
cc = ((b - a).days)
w = datetime.weekday(a)
working_day = []
for i in range(cc + 1):
    if w < 5:
        working_day.append(w)
        w += 1
    elif w > 5:
        w = 0
    else:
        w += 1
print('Number of working day ' + str(len(working_day)))
