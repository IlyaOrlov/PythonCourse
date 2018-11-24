from decimal import Decimal


class Money:
    rub = Decimal("0.00")
    __d_rate = Decimal("0.00")

    def __init__(self, sum):
        self.rub = Decimal(sum).quantize(Decimal("1.00"))

    @property
    def d_rate(self):
        d = self.__d_rate
        if d == Decimal("0.00"):
            print("Dollar rate is not set, use 30 rub/$ by default")
            d = Decimal("30.00")
        return d

    @d_rate.setter
    def d_rate(self, value):
        self.__d_rate = Decimal(value).quantize(Decimal("1.00"))

    def get_in_dollar(self):
        return (self.rub / self.d_rate).quantize(Decimal("1.00"))

# ToString redefention
    def __repr__(self):
        s = str(self.rub)
        return "{} rub. and {} cop.".format(s.split(".")[0], s.split(".")[1])

# equal redefinition
    def __eq__(self, other):
        return self.rub == other.rub

# nonequal redefinition
    def __ne__(self, other):
        return self.rub != other.rub

# less redefinition
    def __lt__(self, other):
        return self.rub < other.rub

# great redefinition
    def __gt__(self, other):
        return self.rub > other.rub

# subtraction redefinition
    def __sub__(self, other):
        return self.rub - other.rub

# sum redefinition
    def __add__(self, other):
        return self.rub + other.rub

# multiply redefinition
    def __mul__(self, other):
        return (self.rub * other.rub).quantize(Decimal("1.00"))

# divide redefinition
    def __truediv__(self, other):
        return (self.rub / other.rub).quantize(Decimal("1.00"))

    def __floordiv__(self, other):
        return self.rub // other.rub

    def __mod__(self, other):
        return self.rub % other.rub


m100 = Money(100)
m10_5 = Money(10.5)
print(m100)
print(m10_5)
print(m10_5 + m100)
print(m100.get_in_dollar())
m100.d_rate = 65.7
print(m100.get_in_dollar())
