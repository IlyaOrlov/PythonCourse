import unittest
from roman import to_roman, NonValidInput


class TestRoman(unittest.TestCase):

    def test_to_roman1(self):
        self.assertEqual(to_roman(5), 'V')

    def test_to_roman2(self):
        self.assertRaises(NonValidInput, to_roman, 0)

    def test_to_roman3(self):
        self.assertRaises(NonValidInput, to_roman, 'not an integer')


if __name__ == '__main__':
    unittest.main()
