import unittest
import roman

class TestRomanFun(unittest.TestCase):
    '''Tests for functions to_roman()'''

    def test_to_roman_positive(self):
        self.assertEqual('I', roman.to_roman(1))
        self.assertEqual('XIII', roman.to_roman(13))
        self.assertEqual('CXI', roman.to_roman(111))
        self.assertEqual('MMI', roman.to_roman(2001))
        self.assertEqual('M_V_CMXCIX', roman.to_roman(4999))
        self.assertEqual('_V_', roman.to_roman(5000))

    def test_to_roman_negative(self):
        with self.assertRaises(roman.NonValidInput):
            roman.to_roman(0)
            roman.to_roman('12')
            roman.to_roman(5000)

    def test_to_roman_no_arg(self):
        with self.assertRaises(TypeError):
            roman.to_roman()


if __name__ == '__main__':
    unittest.main()
