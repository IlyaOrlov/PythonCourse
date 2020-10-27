class Money:
    def __init__(self, value):
        self.rub = int(value // 1)
        self.cop = round(value - self.rub, 2)

    def _value(self):
        return self.rub + self.cop

    def __repr__(self):
        return f"{self.rub},{self.cop * 100:.0f}"

    def __sub__(self, other):
        return Money(self._value() - other._value())

    def __add__(self, other):
        return Money(self._value() + other._value())

    def __mul__(self, other):
        return Money(self._value() * other._value())

    def __truediv__(self, other):
        return Money(self._value() / other._value())

    @staticmethod
    def ratio():
        return 74.09

    @property
    def dollars(self):
        return Money(self._value() / self.ratio())

    def converting(self):
        return self.dollars
