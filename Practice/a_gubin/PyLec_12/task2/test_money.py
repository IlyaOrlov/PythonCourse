import unittest
from money import Money


class TestMoney(unittest.TestCase):
    value = 10205.5
    money = Money(value)

    def test_value(self):
        self.assertEqual(TestMoney.money._value(), TestMoney.value)

    def test_repr(self):
        self.assertEqual(repr(TestMoney.money), "10205,50")

    def test_sub(self):
        self.assertEqual((TestMoney.money - Money(100))._value(), 10105.5)

    def test_add(self):
        self.assertEqual((TestMoney.money + Money(100.5))._value(), 10306.0)

    def test_mul(self):
        self.assertEqual((TestMoney.money * Money(2))._value(), 20411.0)

    def test_truediv(self):
        self.assertEqual((TestMoney.money / Money(2))._value(), 5102.75)

    def test_dollars(self):
        self.assertEqual(TestMoney.money.dollars._value(), round(TestMoney.value / Money.ratio(), 2))

    def test_converting(self):
        self.assertEqual(TestMoney.money.converting()._value(), round(TestMoney.value / Money.ratio(), 2))


if __name__ == '__main__':
    unittest.main()
