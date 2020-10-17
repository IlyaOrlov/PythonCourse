class Money:
    SIGN = "Р"

    def __init__(self, rubles, kopecks=0):
        self._rub = rubles
        self._kop = kopecks

    def __repr__(self):
        return "Money(rubles={}, kopecks={})".format(self._rub, self._kop)

    def __str__(self):
        return "{},{:02d} {}".format(self._rub, self._kop, self.SIGN)

    def __add__(self, other):
        if other is None or not isinstance(other, Money):
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(type(self).__name__, type(other).__name__))
        kop = self._kop + other._kop
        rub = self._rub + other._rub + kop // 100
        kop = kop % 100
        return Money(rub, kop)

    def __sub__(self, other):
        if other is None or not isinstance(other, Money):
            raise TypeError("unsupported operand type(s) for -: '{}' and '{}'".format(type(self).__name__, type(other).__name__))
        kop = self._kop - other._kop
        remainder = 0
        if kop < 0:
            kop = 100 - kop
            remainder = 1
        rub = self._rub - other._rub - remainder
        return Money(rub, kop)

    def _money_to_kopecks(self):
        return self._rub*100 + self._kop

    def __mul__(self, other):
        if other is None or not isinstance(other, Money):
            raise TypeError("unsupported operand type(s) for *: '{}' and '{}'".format(type(self).__name__, type(other).__name__))
        value = self._money_to_kopecks() * other._money_to_kopecks()//100
        rub, kop = divmod(value, 100)
        return Money(rub, kop)

    def __truediv__(self, other):
        if other is None or not isinstance(other, Money):
            raise TypeError("unsupported operand type(s) for *: '{}' and '{}'".format(type(self).__name__, type(other).__name__))
        value = self._money_to_kopecks()/other._money_to_kopecks()
        rub = int(value)
        kop = round((value - rub) * 100)
        return Money(rub, kop)

    def __eq__(self, other):
        if other is None or not isinstance(other, Money):
            return False

        if self._rub == other._rub and self._kop == other._kop:
            return True
        return False

    def __lt__(self, other):
        if other is None or not isinstance(other, Money):
            raise TypeError("operator not supported between instances of '{}' and '{}'".format(type(self).__name__, type(other).__name__))
        if self._money_to_kopecks() < other._money_to_kopecks():
            return True
        return False

    def __gt__(self, other):
        return not (self.__eq__(other) or self.__lt__(other))

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)
