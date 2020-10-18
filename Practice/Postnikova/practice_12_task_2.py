import unittest
import nose

from Money import Money


class TestMoney(unittest.TestCase):
    m1 = Money(100, 50)
    m2 = Money(10, 40)
    m3 = Money(200, 20)
    m4 = Money(400, 4)
    m5 = Money(5, 50)

    def test_equals(self):
        self.assertTrue(self.m1 == self.m1)
        self.assertFalse(self.m1 == self.m2)

    def test_equals_other_type(self):
        self.assertFalse(self.m1 == 12)

    def test_equals_other_none(self):
        self.assertFalse(self.m1 == None)

    def test_not_equal(self):
        self.assertTrue(self.m3 != self.m4)
        self.assertFalse(self.m4 != self.m4)

    def test_add(self):
        m5 = Money(110, 90)
        m6 = Money(600, 24)
        self.assertEqual(m5, self.m1 + self.m2)
        self.assertEqual(self.m2 + self.m1, self.m1 + self.m2)
        self.assertEqual(m6, self.m3 + self.m4)

    def test_add_with_none(self):
        with self.assertRaises(TypeError):
            self.m3 + None

    def test_add_with_other_type(self):
        with self.assertRaises(TypeError):
            self.m3 + 1

    def test_sub(self):
        m5 = Money(90, 10)
        self.assertEqual(m5, self.m1 - self.m2)

    def test_sub_additional(self):
        self.assertEqual(Money(4, 90), self.m2 - self.m5)

    def test_sub_with_none(self):
        with self.assertRaises(TypeError):
            self.m3 - None

    def test_sub_with_other_type(self):
        with self.assertRaises(TypeError):
            self.m1 - 8

        with self.assertRaises(TypeError):
            self.m4 - '333'

    def test_mul(self):
        m5 = Money(1045, 20)
        self.assertEqual(m5, self.m1 * self.m2)

    def test_mul_with_none(self):
        with self.assertRaises(TypeError):
            self.m2 * None

    def test_mul_other_type(self):
        with self.assertRaises(TypeError):
            self.m2 * 50

    def test_truediv(self):
        m5 = Money(19, 25)
        m6 = Money(9, 66)

        self.assertEqual(m5, self.m3/self.m2)
        self.assertEqual(m6, self.m1/self.m2)

    def test_truediv_with_none(self):
        with self.assertRaises(TypeError):
            self.m2/None

    def test_truediv_other_type(self):
        with self.assertRaises(TypeError):
            self.m1/None

    def test_less_than(self):
        self.assertTrue(self.m2 < self.m1)
        self.assertFalse(self.m1 < self.m2)
        self.assertFalse(self.m1 < self.m1)

    def test_less_than_None(self):
        with self.assertRaises(TypeError):
            self.m2 < None

    def test_less_than_other_type(self):
        with self.assertRaises(TypeError):
            self.m3 < 500

    def test_greater_than(self):
        self.assertTrue(self.m4 > self.m1)
        self.assertFalse(self.m1 > self.m4)
        self.assertFalse(self.m1 > self.m1)

    def test_less_equals(self):
        self.assertTrue(self.m1 <= self.m1)
        self.assertTrue(self.m1 <= self.m4)
        self.assertFalse(self.m4 <= self.m1)

    def test_greater_equals(self):
        self.assertTrue(self.m4 >= self.m1)
        self.assertFalse(self.m1 >= self.m4)
        self.assertTrue(self.m4 >= self.m4)


if __name__ == '__main__':
    unittest.main()
