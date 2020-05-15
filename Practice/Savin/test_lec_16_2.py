import unittest
from lec_16_2 import Iterator


class TestIterator(unittest.TestCase):
    def test_iteratio(self):
        iterator = Iterator(10)
        numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        i = 0
        for number in iterator:
            result = numbers[i]
            self.assertEqual(number, result)
            i += 1

    def test_exeption(self):
        with self.assertRaises(StopIteration) as context:
            iteator = Iterator(3)
            for i in range(5):
                next(iteator)


if __name__ == '__main__':
    unittest.main()