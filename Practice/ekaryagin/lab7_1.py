from datetime import datetime, timedelta


def count_work_days(start_date, end_date):

    if start_date > end_date:
        start_date, end_date = end_date, start_date

    delta = (end_date - start_date).days + 1
    result = delta // 7 * 5

    if delta % 7 == 0:
        return result

    weekday_end = end_date.isoweekday()
    weekday_start = (end_date - timedelta(delta % 7)).isoweekday()

    if weekday_start < weekday_end < 6 or weekday_start == 7 and weekday_end < 6:
        return result + delta % 7
    if weekday_end == 6 or weekday_start == 6:
        return result + delta % 7 - 1
    else:
        return result + delta % 7 - 2


if __name__ == "__main__":
    print('сен - ', count_work_days(datetime(2020, 9, 1), datetime(2020, 9, 30)))
    print('окт - ', count_work_days(datetime(2020, 10, 1), datetime(2020, 10, 31)))
    print('ноя - ', count_work_days(datetime(2020, 11, 1), datetime(2020, 11, 30)))
    print('дек - ', count_work_days(datetime(2020, 12, 1), datetime(2020, 12, 31)))
