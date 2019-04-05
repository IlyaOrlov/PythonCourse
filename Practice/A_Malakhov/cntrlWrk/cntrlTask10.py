class Money:
    def __init__(self, rub1, kop1, rub2, kop2):
        self.rub1 = rub1
        self.kop1 = kop1
        self.rub2 = rub2
        self.kop2 = kop2

    def money(self):
        rub_in_kop1 = self.rub1 * 100
        rub1 = rub_in_kop1 // 100 + self.kop1 // 100
        kop1 = rub_in_kop1 % 100 + self.kop1 % 100
        rub_in_kop2 = self.rub2 * 100
        rub2 = rub_in_kop2 // 100 + self.kop2 // 100
        kop2 = rub_in_kop2 % 100 + self.kop2 % 100
        print('Сумма 1 равна: {},{}'.format(rub1, kop1))
        print('Сумма 2 равна: {},{}'.format(rub2, kop2))

    def sum(self):
        sum_rub_in_kop = (self.rub1 + self.rub2) * 100
        sum_kop = self.kop1 + self.kop2
        sum_rub = sum_rub_in_kop // 100 + sum_kop // 100
        kop_in_sum = sum_kop % 100
        print('Результат сложения двух сумм равен: {},{}'.format(sum_rub, kop_in_sum))

    def diff(self):
        if self.rub1 > self.rub2:
            diff_rub_in_kop = (self.rub1 - self.rub2) * 100
        else:
            diff_rub_in_kop = (self.rub2 - self.rub1) * 100
        if self.kop1 > self.kop2:
            diff_kop = self.kop1 - self.kop2
        else:
            diff_kop = self.kop2 - self.kop1
        diff_rub = diff_rub_in_kop // 100 + diff_kop // 100
        kop_in_diff = diff_kop % 100
        print('Разница двух сумм равнa: {},{}'.format(diff_rub, kop_in_diff))

    def multiplication(self):
        sum1 = self.rub1 * 100 + self.kop1
        sum2 = self.rub2 * 100 + self.kop2
        mult_sum = sum1 * sum2
        rub_result = mult_sum // 100 // 100
        kop_result = mult_sum // 100 % 100
        print('Произведение двух сумм равно: {},{}'.format(rub_result, kop_result))

    def division(self):
        sum1 = self.rub1 * 100 + self.kop1
        sum2 = self.rub2 * 100 + self.kop2
        if sum1 > sum2:
            try:
                diff_sum = sum1 / sum2
                print('Результат деления двух сумм равен: {}'.format(diff_sum))
            except ZeroDivisionError:
                print('На ноль делить нельзя')
        else:
            try:
                diff_sum = sum2 / sum1
                print('Результат деления двух сумм равен: {}'.format(diff_sum))
            except ZeroDivisionError:
                print('На ноль делить нельзя')

    def comparison(self):
        sum1 = self.rub1 * 100 + self.kop1
        sum2 = self.rub2 * 100 + self.kop2
        if sum1 > sum2:
            print('Первая сумма больше, чем вторая')
        elif sum2 > sum1:
            print('Вторая сумма больше, чем первая')
        else:
            print('Суммы равны')


m = Money(250, 2225, 20, 220)
m.money()
m.sum()
m.diff()
m.multiplication()
m.division()
m.comparison()


class Currency(Money):
    def us_dollar(self):
        usd = 64.73
        # Курс доллара на 31.01.2019
        rub_in_kop1 = self.rub1 * 100
        sum1 = rub_in_kop1 + self.kop1
        dollar1 = int(sum1 * usd // 100)
        cent1 = int(sum1 * usd % 100)
        rub_in_kop2 = self.rub2 * 100
        sum2 = rub_in_kop2 + self.kop2
        dollar2 = int(sum2 * usd // 100)
        cent2 = int(sum2 * usd % 100)
        print('Первая сумма в USD равна: {},{}'.format(dollar1, cent1))
        print('Вторая сумма в USD равна: {},{}'.format(dollar2, cent2))

    def euro(self):
        euro = 72.72
        # Курс евро на 31.03.2019
        rub_in_kop1 = self.rub1 * 100
        sum1 = rub_in_kop1 + self.kop1
        euro1 = int(sum1 * euro // 100)
        cent1 = int(sum1 * euro % 100)
        rub_in_kop2 = self.rub2 * 100
        sum2 = rub_in_kop2 + self.kop2
        euro2 = int(sum2 * euro // 100)
        cent2 = int(sum2 * euro % 100)
        print('Первая сумма в EURO равна: {},{}'.format(euro1, cent1))
        print('Вторая сумма в EURO равна: {},{}'.format(euro2, cent2))


c = Currency(25, 85, 50, 5235)
c.us_dollar()
c.euro()
