import datetime
import sys


def work_days_counter(day1, day2):
    weeks = (day2 - day1).days // 7
    work_days = weeks * 5
    day = day1 + datetime.timedelta(days=weeks * 7)
    for i in range((day2 - day).days):
        if (day + datetime.timedelta(days=i)).weekday() < 5:
            work_days += 1
    return work_days


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Enter dates using format: YYYY-MM-DD")
        d1 = datetime.date.fromisoformat(input("from (include): "))
        d2 = datetime.date.fromisoformat(input("to (exclude): "))
    else:
        d1 = datetime.date.fromisoformat(sys.argv[1])
        d2 = datetime.date.fromisoformat(sys.argv[2])
    print(work_days_counter(d1, d2))
