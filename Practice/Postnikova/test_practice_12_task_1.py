from unittest import TestCase, main

from practice_12_task_1 import to_roman, NonValidInput


class TestToRoman(TestCase):
    def test_simple_number(self):
        self.assertEqual('III', to_roman(3))

    def test_decades(self):
        self.assertEqual('XLV', to_roman(45))

    def test_hundreds(self):
        self.assertEqual('DCXXXIV', to_roman(634))

    def test_thousands(self):
        self.assertEqual('MMMDXXI', to_roman(3521))

    def test_middle_zero(self):
        self.assertEqual('CDIV', to_roman(404))

    def test_ending_zero(self):
        self.assertEqual('CC', to_roman(200))

    def test_edge_cases(self):
        self.assertEqual('I', to_roman(1))
        self.assertEqual('\u2181', to_roman(5000))

    def test_non_valid_input(self):
        with self.assertRaises(NonValidInput):
            to_roman(0)

        with self.assertRaises(NonValidInput):
            to_roman(5001)

if __name__ == '__main__':
    main()

