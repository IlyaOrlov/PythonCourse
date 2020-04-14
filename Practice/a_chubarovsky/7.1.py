import datetime


def workdays(date1, date2):
    if date1 < date2:
        count = 0
        date = date1
        while True:
            if date1 <= date <= date2:
                if date.weekday() != 5 and date.weekday() != 6:
                    count += 1
                date += datetime.timedelta(days=1)
            else:
                break
        return count
    else:
        print("Введён некорректный временной промежуток.")


if __name__ == "__main__":
    try:
        a, b, c = map(int, input("Введите начальную дату (ГГГГ/ММ/ДД): ").split())
        e, f, g = map(int, input("Введите конечную дату (ГГГГ/ММ/ДД): ").split())
        begin = datetime.date(a, b, c)
        end = datetime.date(e, f, g)
        work = workdays(begin, end)
        print("Количество рабочих дней в заданном промежутке = {}.".format(work))
    except ValueError:
        print("Введена некорректная дата.")
