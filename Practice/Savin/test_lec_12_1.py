import unittest

from lec_12_1 import NonValidInput, to_roman


class TestToRoman(unittest.TestCase):
    def test_exeption(self):
        self.assertRaises(NonValidInput, to_roman, 5001)

    def test_number_1(self):
        number = 10
        result = to_roman(number)
        self.assertEqual(result, 'X')

    def test_number_2(self):
        number = 453
        result = to_roman(number)
        self.assertEqual(result, 'CDLIII')

    def test_number_3(self):
        number = 1294
        result = to_roman(number)
        self.assertEqual(result, 'MCCXCIV')

    def test_number_4(self):
        number = 3150
        result = to_roman(number)
        self.assertEqual(result, 'MMMCL')

    def test_number_5(self):
        number = 4782
        result = to_roman(number)
        self.assertEqual(result, 'MUDCCLXXXII')

if __name__ == '__main__':
    unittest.main()