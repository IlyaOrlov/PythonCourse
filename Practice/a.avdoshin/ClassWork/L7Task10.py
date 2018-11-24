# 22.11 - [ИО]:  Проверено (есть замечания) - пока 5 баллов из 7.
from enum import Enum


class Currency(Enum):
    RUB = 1.
    USD = 66.
    EUR = 75.
    JPY = 2.


class Money:
    def __init__(self, value=0, cur=Currency.RUB):
        self.__currency = cur
        # 22.11 - [ИО]:  пересчитывать произведение констант в каждой функции
        # очень неэффективно 100 * self.__currency.value
        self.__value = 100 * value * self.__currency.value

    def __add__(self, other):
        self.__value += int(100 * other.value * other.cur.value)
        # 22.11 - [ИО]:  а как же стиль? 79 символовв строке!
        return Money(self.__value / (100 * self.__currency.value), self.__currency)

    def __sub__(self, other):
        self.__value -= int(100 * other.value * other.cur.value)
        return Money(self.__value / (100 * self.__currency.value), self.__currency)

    def __mul__(self, other):
        return Money(self.__value * other / (100 * self.__currency.value), self.__currency)

    def __truediv__(self, other):
        return Money(self.__value / (100 * self.__currency.value * other), self.__currency)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '{:.2f} {}'.format(self.__value / (100 * self.__currency.value), self.__currency.name)

    @property
    def value(self):
        return self.__value / (100 * self.__currency.value)

    @property
    def cur(self):
        return self.__currency


a = Money(10.86, Currency.USD)
b = Money(1.76, Currency.EUR)
c = Money(1.28, Currency.RUB)
d = Money(3, Currency.JPY)
print(a - b + c*3 + d/2)

