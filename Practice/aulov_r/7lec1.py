import datetime

a = input('Первая дата (гггг-мм-дд): ')
b = input('Вторая дата (гггг-мм-дд): ')
a = a.split('-')
b = b.split('-')
aa = datetime.date(int(a[0]), int(a[1]), int(a[2]))
bb = datetime.date(int(b[0]), int(b[1]), int(b[2]))
cc = aa - bb
print(cc)  # output days and time
dd = str(cc)
print(dd.split()[0])  # only days