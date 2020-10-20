import unittest
from money import Money as Money


class TestMoneyClass(unittest.TestCase):
    '''Tests for class Money'''

    # shared class instances for testing methods
    m1 = Money(12, 145)
    m2 = Money(7, 63)
    m3 = Money(2, 3)
    m5 = Money(2, 35)
    m4 = Money(1, 45)

    def test_init(self):
        self.assertEqual(13, self.m1._Money__ru)          # m1 - conversion in init, cash = 13,45
        self.assertEqual(45, self.m1._Money__kop)
        self.assertEqual(1, self.m4._Money__ru)           # m4 - standard data
        self.assertEqual(45, self.m4._Money__kop)

    def test_str(self):
        self.assertEqual('13,45', self.m1.__str__())
        self.assertEqual('2,03', self.m3.__str__())

    def test_add(self):
        m_past_add = self.m1+self.m2
        self.assertEqual('21,08', m_past_add.__str__())

    def test_sub(self):
        m_1_2 = self.m1 - self.m2
        m_2_1 = self.m2 - self.m1
        m_2_3 = self.m2 - self.m3
        m_4_2 = self.m4 - self.m2
        m_3_5 = self.m3 - self.m5
        m_5_3 = self.m5 - self.m3
        self.assertEqual('5,82', m_1_2.__str__())       # 13,45 - 7,63 =  5,82
        self.assertEqual('-5,82', m_2_1.__str__())      # 7,63 - 13,45 = -5,82
        self.assertEqual('5,60', m_2_3.__str__())       # 7,63 - 2,03 = 5,60
        self.assertEqual('-6,18', m_4_2.__str__())      # 1,45 - 7,63 = -6,18
        self.assertEqual('-0,32', m_3_5.__str__())      # 2,3 - 2,35 = -0,32
        self.assertEqual('0,32', m_5_3.__str__())       # 2,35 - 2,03 = 0,32

    def test_truediv(self):
        m_2_4 = self.m2 / self.m4
        m_5_1 = self.m5 / self.m1
        m_infinity = self.m5 / Money(0, 0)
        self.assertEqual('5.2621', m_2_4.__str__())
        self.assertEqual('0.1747', m_5_1.__str__())
        self.assertEqual('Infinity', m_infinity.__str__())

    def test_lt(self):
        self.assertTrue(self.m4 < self.m1)
        self.assertFalse(self.m5 < self.m3)

    def test_le(self):
        self.assertTrue(self.m3 <= self.m5)
        self.assertTrue(self.m3 <= self.m3)
        self.assertFalse(self.m5 <= self.m3)

    def test_eq(self):
        self.assertTrue(self.m5 == self.m5)
        self.assertFalse(self.m5 == self.m4)

    def test_ne(self):
        self.assertTrue(self.m5 != self.m3)
        self.assertFalse(self.m5 != self.m5)

    def test_gt(self):
        self.assertTrue(self.m1 > self.m5)
        self.assertFalse(self.m5 > self.m1)

    def test_ge(self):
        self.assertTrue(self.m5 >= self.m5)
        self.assertTrue(self.m5 >= self.m3)
        self.assertFalse(self.m5 >= self.m2)

    def test_change_to_dollars(self):
        m_to_dollars = Money(345634, 175).change_to_dollars()
        self.assertEqual('4594.3872', m_to_dollars.__str__())


if __name__ == '__main__':
    unittest.main()
