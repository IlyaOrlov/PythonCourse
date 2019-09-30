import datetime


class Period():
    # Нерабочие праздничный дни
    holiday=("01-01","01-02","01-03","01-04","01-05","01-06","01-07","01-08"
                  "02-23","03-08","05-01","05-09","06-12","11-14",
             )
    # Переносы на рабочие дни 2019
    holiday_work={'2019-05-04'}
    work_holiday={'2019-05-06'}

    def __init__(self, begin, end):
        self.begin=begin
        self.end=end

    @staticmethod
    def validate(text):
        try:
            datetime.datetime.strptime(text, '%d.%m.%Y')
        except ValueError:
            text =None
        return text

    def period(self):
        begin=Period.validate(self.begin)
        end=Period.validate(self.end)
        if begin==None or end==None:
            return print("Неправильный формат даты, должен быть дд.мм.гггг.")
        else:
            begin=datetime.datetime.strptime(begin,'%d.%m.%Y')
            end=datetime.datetime.strptime(end,'%d.%m.%Y')
        delta = datetime.timedelta(days=1)
        sum=0
        while begin <= end:
            # Количество понедельников - пятниц.
            if begin.isoweekday()<6:
                sum += 1
               # print("Рабочие дни: {}". format(begin))
            # Минус нерабочие праздничные дни
            if str(begin)[5:10] in Period.holiday:
                sum -= 1
               #print("Праздники: {}". format(str(begin)[0:10]))
            # Переносы с рабочих на нерабочие
            if str(begin)[0:10] in Period.holiday_work:
                #print("Перенос  с рабочих на нерабочие: {}". format(str(begin)[0:10]))
                sum += 1
            # Переносы с нерабочих на рабочие
            if str(begin)[0:10] in Period.work_holiday:
               # print("Перенос с нерабочих на рабочие: {}". format(str(begin)[0:10]))
                sum -= 1
            begin += delta
        return sum


date_begin="01.01.2019"
date_end="31.12.2019"
a=Period(date_begin,date_end)
print("Количество рабочих дней в период с {} по {} составляет: {}".
        format(date_begin,date_end,a.period()))