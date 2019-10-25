from datetime import date,timedelta

def workdayscount(fromdate, todate):


    daygenerator = (fromdate + timedelta(x) for x in range((todate - fromdate).days + 1))
    res = sum(1 for day in daygenerator if day.weekday() < 5)
    print(res)
print(workdayscount(date(2019, 10, 24), date(2019, 10, 31)))