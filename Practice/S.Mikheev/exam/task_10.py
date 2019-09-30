class Money:
    __slots__ = ["_value", "_currency"]
    dollar_rate = None

    def __init__(self, value, currency):
        if currency in ['RUB', 'USD']:
            self._value = value
            self._currency = currency
        else:
            print('incorrect currency. Choose USD or RUB')

    @property
    def value(self):
        return self._value

    @property
    def currency(self):
        return self._currency

    def __repr__(self):
        return '{} {}'.format(str(int(self.value)) + "," +
                              str('{:.2f}'.format(self.value).split('.')[1]), self.currency)

    def __add__(self, other):
        if isinstance(other, Money):
            self._assert_currency(other)
            # self._value = self.value + other.value
            return Money(self.value + other.value, self.currency)
        else:
            return Money(float(self.value + other), self.currency)

    def __sub__(self, other):
        if isinstance(other, Money):
            self._assert_currency(other)
            # self._value = self.value - other.value
            return Money(self.value - other.value, self.currency)
        else:
            return Money(float(self.value - other), self.currency)

    def __truediv__(self, other):
        if isinstance(other, Money):
            self._assert_currency(other)
            if other.value == 0:
                raise ZeroDivisionError
            return Money(self.value / other.value, self.currency)
        else:
            if other == 0:
                raise ZeroDivisionError
            return Money(float(self.value / other), self.currency)

    def __lt__(self, other):
        if isinstance(other, Money):
            self._assert_currency(other)
            return self.value < other.value

    def transfer(self):
        if self.currency == 'RUB':
            self._value /= Money.dollar_rate
            self._currency = 'USD'
            print('Transfered RUB to USD')
        elif self.currency == 'USD':
            self._value *= Money.dollar_rate
            self._currency = 'RUB'
            print('Transfered USD to RUB')

    def _assert_currency(self, other):
        if self.currency != other.currency:
            raise CurrencyError


class CurrencyError(ValueError):
    def __init__(self):
        super().__init__('Different currency')


a = Money(10.5, 'USD')
print(a)
b = Money(80.5, 'RUB')
print(b)
Money.dollar_rate = 64.66
a.transfer()
print(a)
c = a + b
print(c)
d = a - b
print(d)
print('{} > {}: {}'.format(c.value, d.value, c > d))
print('{} / {} = {}'.format(c.value, 3, c / 3))
print(c)
e = c + 1000
print(e)
print(c)
print(c > e)
