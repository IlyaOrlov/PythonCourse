class Money:

    def __init__(self, rub: int, kop: int):
        if kop > 99:
            raise TypeError(f'Должно быть не больше 99коп. Задали {kop}')
        if rub < 0:
            self._abs = -(abs(rub) * 100 + kop)
        else:
            self._abs = rub * 100 + kop
        self._rub = rub
        self._kop = kop

        self._kurs = 74.13

    def __str__(self):
        if len(str(self._kop)) > 1 and str(self._kop).isalnum():
            return f'{self._rub},{self._kop}'
        else:
            return f'{self._rub},0{self._kop}'

    def __lt__(self, other):
        return abs(self._abs) < abs(other._abs)

    def __le__(self, other):
        return abs(self._abs) <= abs(other._abs)

    def __eq__(self, other):
        return abs(self._abs) == abs(other._abs)

    def __ne__(self, other):
        return abs(self._abs) != abs(other._abs)

    def __gt__(self, other):
        return abs(self._abs) > abs(other._abs)

    def __ge__(self, other):
        return abs(self._abs) >= abs(other._abs)

    def __add__(self, other):
        result = self._abs + other._abs
        return self.convert(result)

    def __sub__(self, other):
        result = self._abs - other._abs
        return self.convert(result)

    def __mul__(self, other):
        result = self._abs * other
        return self.convert(result)

    def __truediv__(self, other):
        if isinstance(other, Money):
            result = round(self._abs / other._abs, 2)
            return result
        else:
            result = int(self._abs / other)
            return self.convert(result)

    def convert(self, abs):
        if abs > 99:
            rub = abs // 100
            kop = abs % 100
            return Money(rub, kop)
        elif abs < -99:
            rub = -(-abs // 100)
            kop = -abs % 100
            return Money(rub, kop)
        else:
            rub = 0
            kop = abs
            return Money(rub, kop)

    def rub_in_usd(self):
        result = round(self._abs / 100 / self._kurs, 2)
        return result



m1 = Money(1000, 50)
m2 = Money(500, 50)

print(m1-m2)
print(m1+m2)
print(m1/m2)
print(m1*2)
print(m1/2)
print(m1.rub_in_usd())



