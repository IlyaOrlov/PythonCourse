class Money:
    usd_rate = 65.15

    def __init__(self, rub, kop):
        self.rub = rub
        self.kop = kop

    def to_kop(self):
        return self.rub * 100 + self.kop

    def __str__(self):
        return '{},{}'.format(self.rub, self.kop)

    # Сложение

    def __add__(self, other):
        rub = self.rub + other.rub
        kop = self.kop + other.kop
        if kop > 100:
            rub += kop // 100
            kop = kop % 100
        return Money(rub, kop)

    # Вычитание

    def __sub__(self, other):
        if self > other:
            kop = self.to_kop() - other.to_kop()
            rub = kop // 100
            kop = kop % 100
            return Money(rub, kop)
        else:
            return None

    # Деление

    def __truediv__(self, other):
        if other.to_kop() == 0:
            return None
        else:
            kop = self.to_kop() / other.to_kop()
            return Money(int(kop // 100), int(kop % 100))

    # Сравнение

    def __gt__(self, other):
        return self.to_kop() > other.to_kop()

    # Перевод в доллар

    def convert_usd(self):
        usd = self.to_kop() * self.usd_rate / 100
        return round(usd, 2)


a = Money(17, 50)
b = Money(3,76)

print(f'RUB {a}')
print(f'RUB {b}')

c = a + b
print(f'{a} RUB + {b} RUB = {c} RUB')

d = a - b
print(f'{a} RUB - {b} RUB = {d} RUB')

e = a / b
print(f'{a} RUB / {b} RUB = {e}')

f = a.convert_usd()
print(f'{a} RUB = {f} USD')

if a > b:
    print(f'{a} RUB > {b} RUB')
else:
    print(f'{b} RUB > {a} RUB')
