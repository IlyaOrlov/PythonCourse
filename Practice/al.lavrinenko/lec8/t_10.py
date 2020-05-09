class Money:
    _exchange_rate = 74.53

    def __init__(self, rub, kop):
        if not isinstance(rub, int) or not isinstance(kop, int):
            raise TypeError('Both arguments must be integers')
        if rub > 0 > kop or rub < 0 < kop:
            raise ValueError('Both arguments must be either non-positive or '
                             'non-negative at the same time')
        if abs(kop) > 99:
            raise ValueError('The absolute value of the 2nd argument must be '
                             'lower than 100')
        self._rub = rub
        self._kop = kop

    @staticmethod
    def create_by_kop(kop):
        abs_rub = abs(kop) // 100
        abs_kop = abs(kop) % 100
        if kop >= 0:
            return Money(abs_rub, abs_kop)
        else:
            return Money(-abs_rub, -abs_kop)

    def get_in_kop(self):
        return self._rub*100 + self._kop

    def to_usd(self):
        return f'{self.get_in_kop()/100/Money._exchange_rate:.2f}'

    def __repr__(self):
        return f'{self._rub + self._kop/100:.2f}'.replace('.', ',')

    def __eq__(self, other):
        return self.get_in_kop() == other.get_in_kop()

    def __ne__(self, other):
        return self.get_in_kop() != other.get_in_kop()

    def __lt__(self, other):
        return self.get_in_kop() < other.get_in_kop()

    def __gt__(self, other):
        return self.get_in_kop() > other.get_in_kop()

    def __le__(self, other):
        return self.get_in_kop() <= other.get_in_kop()

    def __ge__(self, other):
        return self.get_in_kop() >= other.get_in_kop()

    def __add__(self, other):
        return Money.create_by_kop(self.get_in_kop() + other.get_in_kop())

    def __sub__(self, other):
        return Money.create_by_kop(self.get_in_kop() - other.get_in_kop())

    def __truediv__(self, other):
        if isinstance(other, Money):
            return self.get_in_kop() / other.get_in_kop()
        else:
            return Money.create_by_kop(round(self.get_in_kop() / other))


m1 = Money(89, 50)
m2 = Money(100, 88)
print(m2 - m1)
print(m2 / m1)
print(m1 >= m2)
print(m2.to_usd())
