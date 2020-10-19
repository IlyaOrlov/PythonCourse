import unittest
from task1 import rome_converter


class TestToRoman(unittest.TestCase):

    def test_invalid_input_range(self):
        with self.assertRaises(rome_converter.NotValidInput):
            rome_converter.to_roman(5001)
        with self.assertRaises(rome_converter.NotValidInput):
            rome_converter.to_roman(0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            rome_converter.to_roman(60.4)
        with self.assertRaises(TypeError):
            rome_converter.to_roman("200")

    def test_converting(self):
        self.assertEqual(rome_converter.to_roman(4000), "MMMM")
        self.assertEqual(rome_converter.to_roman(200), "CC")
        self.assertEqual(rome_converter.to_roman(581), "DLXXXI")
        self.assertEqual(rome_converter.to_roman(1076), "MLXXVI")


if __name__ == '__main__':
    unittest.main()
