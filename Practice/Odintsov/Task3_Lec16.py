import unittest
import Task2_Lec16

class TestGetItem(unittest.TestCase):

    def setUp(self):
        print("Start test")

    def test_Equal_result(self):
        self.assertEqual(Task2_Lec16.PrimeNumber(10).__getitem__(), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def tearDown(self):
        print("End test")

if __name__ == '__main__':
    unittest.main()