import datetime


def calc_holydays(start, end):
    return int((end - start).days * 2/7)


print(calc_holydays(datetime.date(2012, 12, 14), datetime.date(2013, 12, 14)))
