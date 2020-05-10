import unittest

from class_Money import Money


class TestMoney(unittest.TestCase):
    def test_exeption(self):
        self.assertRaises(TypeError, Money, 5001)

    def test_less(self):
        a = Money(5, 30)
        b = Money(10, 50)
        self.assertTrue(a < b)

    def test_less_or_equal(self):
        a = Money(5, 30)
        b = Money(10, 50)
        self.assertTrue(a <= b)

    def test_equal(self):
        a = Money(10, 50)
        b = Money(10, 50)
        self.assertEqual(a, b)

    def test_not_equal(self):
        a = Money(5, 30)
        b = Money(10, 50)
        self.assertNotEqual(a, b)

    def test_more(self):
        a = Money(10, 50)
        b = Money(5, 30)
        self.assertTrue(a > b)

    def test_more_or_equal(self):
        a = Money(10, 50)
        b = Money(5, 30)
        self.assertTrue(a >= b)

    def test_add(self):
        a = Money(10, 60)
        b = Money(5, 80)
        c = Money(16, 40)
        result = a + b
        self.assertEqual(result, c)

    def test_sub(self):
        a = Money(10, 60)
        b = Money(5, 80)
        c = Money(4, 80)
        result = a - b
        self.assertEqual(result, c)

    def test_mul(self):
        a = Money(10, 60)
        b = Money(53, 0)
        result = a * 5
        self.assertEqual(result, b)

    def test_truediv_number(self):
        a = Money(10, 60)
        b = Money(2, 12)
        result = a / 5
        self.assertEqual(result, b)

    def test_truediv_money(self):
        a = Money(10, 60)
        b = Money(5, 20)
        c = 2.04
        result = a / b
        self.assertEqual(result, c)

if __name__ == '__main__':
    unittest.main()