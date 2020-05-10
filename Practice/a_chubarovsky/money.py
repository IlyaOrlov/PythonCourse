def int_r(num):  # функция для классического округления
    num = int(num + (0.5 if num > 0 else -0.5))
    return num


class Money:

    def __init__(self, rubles, pennies, exchange_rate=None):
        if not isinstance(rubles, int) and not isinstance(pennies, int):
            raise TypeError('Rubles and pennies expected to be Integer.')
        elif pennies not in range(0, 100):
            raise ValueError('Pennies expected to be in range 0 to 99.')
        elif exchange_rate is not None and not isinstance(exchange_rate, float):
            raise TypeError('Exchange rate expected to be Integer.')
        self.rubles = rubles
        self.pennies = pennies
        self.exchange_rate = exchange_rate

    def __str__(self):
        if self.exchange_rate is None:
            return f'{self.rubles} rubles, {self.pennies} pennies.'
        else:
            return f'{self.rubles} dollars, {self.pennies} cents.'

    def __add__(self, other):
        plus_rubles = self.rubles + other.rubles
        plus_pennies = self.pennies + other.pennies
        plus_rubles += plus_pennies // 100
        plus_pennies = plus_pennies % 100
        return Money(plus_rubles, plus_pennies)

    def __sub__(self, other):
        minus_rubles = self.rubles - other.rubles
        minus_pennies = self.pennies - other.pennies
        minus_rubles -= minus_pennies // 100
        minus_pennies = minus_pennies % 100
        return Money(minus_rubles, minus_pennies)

    def __truediv__(self, other):
        divided = (self.rubles * 100 + self.pennies) / (other.rubles * 100 + other.pennies)
        div_rubles = int(divided)
        div_pennies = int_r((divided - div_rubles) * 100)
        return Money(div_rubles, div_pennies)

    def __mul__(self, other):
        multiple = float((self.rubles * 100 + self.pennies) / 100) * ((other.rubles * 100 + other.pennies) / 100)
        mul_rubles = int(multiple)
        mul_pennies = int_r((multiple - mul_rubles) * 100)
        return Money(mul_rubles, mul_pennies)

    def __lt__(self, other):
        if self.rubles < other.rubles and self.pennies < other.pennies:
            return True
        else:
            return False

    def __le__(self, other):
        if self.rubles <= other.rubles and self.pennies <= other.pennies:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.rubles == other.rubles and self.pennies == other.pennies:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.rubles != other.rubles and self.pennies != other.pennies:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.rubles > other.rubles and self.pennies > other.pennies:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.rubles >= other.rubles and self.pennies >= other.pennies:
            return True
        else:
            return False

    def convert(self):
        converted = (self.rubles * 100 + self.pennies) / (self.exchange_rate * 100)
        conv_dollars = int(converted)
        conv_cents = int_r((converted - conv_dollars) * 100)
        return Money(conv_dollars, conv_cents, self.exchange_rate)
