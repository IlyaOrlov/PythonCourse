import unittest
from money import Money


class TestMoney(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.m1 = Money(10, 55)
        cls.m2 = Money(5, 35)
        cls.m3 = Money(73, 44, 73.44)
        print(f'Starting test class Money with attributes:\n{cls.m1};\n{cls.m2};\n{cls.m3}')

    def test_money1(self):
        self.assertRaises(TypeError, Money, 10.0, 20.0)

    def test_money2(self):
        self.assertRaises(ValueError, Money, 10, 110)

    def test_money3(self):
        self.assertRaises(TypeError, Money, 10, 20, 30)

    def test_money4(self):
        self.assertEqual(str(self.m1 + self.m2), '15 rubles, 90 pennies.')

    def test_money5(self):
        self.assertEqual(str(self.m1 - self.m2), '5 rubles, 20 pennies.')

    def test_money6(self):
        self.assertEqual(str(self.m1 / self.m2), '1 rubles, 97 pennies.')

    def test_money7(self):
        self.assertEqual(str(self.m1 * self.m2), '56 rubles, 44 pennies.')

    def test_money8(self):
        self.assertTrue(self.m2 < self.m1)
        self.assertFalse(self.m1 < self.m2)
        self.assertFalse(self.m1 < self.m1)

    def test_money9(self):
        self.assertTrue(self.m2 <= self.m1)
        self.assertFalse(self.m1 <= self.m2)
        self.assertTrue(self.m1 <= self.m1)

    def test_money10(self):
        self.assertTrue(self.m1 == self.m1)
        self.assertFalse(self.m1 == self.m2)

    def test_money11(self):
        self.assertTrue(self.m1 != self.m2)
        self.assertFalse(self.m1 != self.m1)

    def test_money12(self):
        self.assertTrue(self.m1 > self.m2)
        self.assertFalse(self.m2 > self.m1)
        self.assertFalse(self.m1 > self.m1)

    def test_money13(self):
        self.assertTrue(self.m1 >= self.m2)
        self.assertFalse(self.m2 >= self.m1)
        self.assertTrue(self.m1 >= self.m1)

    def test_money14(self):
        self.assertEqual(str(self.m3.convert()), '1 dollars, 0 cents.')


if __name__ == '__main__':
    unittest.main()
