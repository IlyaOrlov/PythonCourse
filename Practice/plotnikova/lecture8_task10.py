import requests
from bs4 import BeautifulSoup


class Money:
    def __init__(self, r, k, c):
        self.r =r
        self.k =k
        self.cur =c
        self.x = eval(str(self.r) + "." + str(self.k))
        self.course = self.getCourse() if self.cur == "USD" else 1
        self.rub_cur = self.x * self.course

    def get_num(self, data):
        return str(data).replace('.',',')


    # Сложение
    def __add__(self, other):
        return str('%.2f' % (self.rub_cur+other.rub_cur)).replace('.',',')

    # Вычитание
    def __sub__(self, other):
        return  str('%.2f' % (self.rub_cur-other.rub_cur)).replace('.',',')

    # Деление
    def __truediv__(self, other):
        return  str('%.2f' % (self.rub_cur/other.rub_cur)).replace('.',',')

    # Сравнение
    def __lt__(self, other):
        return self.rub_cur < other.rub_cur

    def __le__(self, other):
        return self.rub_cur <= other.rub_cur

    def __eq__(self, other):
        return self.rub_cur == other.rub_cur

    def __ne__(self, other):
        return self.rub_cur != other.rub_cur

    def __gt__(self, other):
        return self.rub_cur > other.rub_cur

    def __ge__(self, other):
        return self.rub_cur>= other.rub_cur

    def getCourse(self):
        url = "https://cbr.ru/currency_base/daily/"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, features="html.parser")
        soup=soup.select('table.data tr')

        for row in list(soup):
            cols = row.find_all('td')
            if len(cols)>0 and cols[1].text=='USD':
                return float((cols[4].text).replace(',','.'))

        return 1


x=Money(1,00, "USD")
y=Money(10,00, "RUB")
print("Курс = ",x.course)

print("x = ",x.get_num(x.x), x.cur)
print("y = ",y.get_num(y.x), y.cur)
print("x = ",x.get_num(x.rub_cur), " RUB")
print("y = ",y.get_num(y.rub_cur), " RUB")
print("x+y = ",x+y, " RUB")
print("x-y = ",x-y, " RUB")
print("x/y: ",x/y, " RUB")
print("x<y: ",x<y)
print("x<=y: ",x<=y)
print("x==y: ",x==y)
print("x!=y: ",x!=y)
print("x>y: ",x>y)
print("x>=y: ",x>=y)
