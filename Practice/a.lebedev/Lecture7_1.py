import datetime


def Dateinput():
    y = int(input('year ='))
    m = int(input('month ='))
    d = int(input('day ='))
    dt = datetime.date(y, m, d)
    return dt


def Datecomp(a, b):
    s = 0
    while a < b:
        if a.isoweekday() in range(1,5):
            s += 1
        else:
            s += 0
        a += datetime.timedelta(days = 1)
    return s

print('Working day in period =', Datecomp(Dateinput(), Dateinput()))

