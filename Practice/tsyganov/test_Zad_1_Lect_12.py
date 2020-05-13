import unittest
from tusk import to_roman, NotValidInput
from nose.tools import assert_equals, raises

class TestTasks(unittest.TestCase):
    def test_to_roman(self):
        self.assertEqual(to_roman(1), 'I')
        self.assertEqual(to_roman(10), 'X')
        self.assertNotEqual(to_roman(8), 'II')
        self.assertRaises(NotValidInput, to_roman,'5')
        self.assertRaises(NotValidInput, to_roman, 11)
        self.assertRaises(NotValidInput, to_roman, [1, 2])

if __name__ == '__main__':
    unittest.main()