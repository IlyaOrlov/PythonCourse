import math


class Money:

    course = 75.23                              # attribute of class. 1 $ = 75,23 rub

    def __init__(self, ru, kop):
        self.__ru = ru

        if kop > 100:                           # if construction gets kop > 100
            self.__ru += kop // 100
            self.__kop = kop % 100
        else:
            self.__kop = kop

    def __str__(self):
        if self.__kop > 10:
            return f'{self.__ru},{self.__kop}'

        elif self.__kop < 0:                    # after magical methods we can have kop < 0
            return f'-{self.__ru},{(-1)*self.__kop}'

        return f'{self.__ru},0{self.__kop}'     # if we have kop < 10 and we need "rub,0{kop}"

    def __add__(self, other):
        return Money(self.__ru + other.__ru + (self.__kop + other.__kop)//100, (self.__kop + other.__kop) % 100)

    def __sub__(self, other):
        buf = round((self.__ru + (self.__kop)/100) - (other.__ru + (other.__kop)/100), 2)   # use float

        if buf < -1:
            return Money(math.trunc(buf), round(buf % math.trunc(buf)*(-100)))

        elif buf < 1 and buf > -1:
            return Money(0, round(buf * (100)))

        return Money(math.trunc(buf), round(buf % math.trunc(buf)*100))

    def __truediv__(self, other):   # " \ " , return float with tile = 4 chars
        if other.__ru != 0 and other.__kop != 0:
            return round((self.__ru + (self.__kop) / 100)/(other.__ru + (other.__kop) / 100), 4)
        return "Infinity"          # or trow ZeroDivisionError

    def __lt__(self, other):       # <
        if self.__ru < other.__ru or (self.__ru == other.__ru and self.__kop < other.__kop):
            return True
        return False

    def __le__(self, other):      # <=
        if self.__ru < other.__ru or (self.__ru == other.__ru and self.__kop <= other.__kop):
            return True
        return False

    def __eq__(self, other):      # ==
        if self.__ru == other.__ru and self.__kop == other.__kop:
            return True
        return False

    def __ne__(self, other):     # !=
        if self.__ru != other.__ru or self.__kop != other.__kop:
            return True
        return False

    def __gt__(self, other):     # >
        if self.__ru > other.__ru or (self.__ru == other.__ru and self.__kop > other.__kop):
            return True
        return False

    def __ge__(self, other):    # >=
        if self.__ru > other.__ru or (self.__ru == other.__ru and self.__kop >= other.__kop):
            return True
        return False

    def change_to_dollars(self):
        return round((self.__ru+(self.__kop/100))/Money.course, 4)
