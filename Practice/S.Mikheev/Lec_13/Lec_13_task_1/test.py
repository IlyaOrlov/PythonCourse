import unittest
from to_roman import to_roman, NonValidInput


class TestToRoman(unittest.TestCase):
    def setUp(self):
        print('test case start')

    def test_to_roman(self):
        print('test to_roman start')
        test_numbers = {2: 'II',
                        3: 'III',
                        4: 'IV',
                        87: 'LXXXVII',
                        88: 'LXXXVIII',
                        89: 'LXXXIX',
                        90: 'XC',
                        91: 'XCI',
                        92: 'XCII',
                        93: 'XCIII',
                        94: 'XCIV',
                        95: 'XCV',
                        96: 'XCVI',
                        97: 'XCVII',
                        98: 'XCVIII',
                        99: 'XCIX',
                        100: 'C'}
        for number in test_numbers:
            self.assertEqual(to_roman(number), test_numbers[number])

    def test_to_roman2(self):
        print('test to_roman2 start')
        with self.assertRaises(NonValidInput):
            to_roman('number')

    def test_to_roman3(self):
        print('test to_roman3 start')
        with self.assertRaises(NonValidInput):
            to_roman(5621)

    def tearDown(self):
        print('test case end')


if __name__ == '__main__':
    # обеспечиваем возможность запуска тестового скрипта из консоли
    unittest.main()
