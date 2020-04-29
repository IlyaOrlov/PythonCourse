import unittest
from tasks import mylen, myrange


class TestTasks(unittest.TestCase):

    def test_mylen(self):
        l = [1, 45, 32, 9]
        self.assertEqual(mylen(l), 4)

    def test_myrange(self):
        self.assertEqual(myrange(5), list(range(5)))
        self.assertEqual(myrange(10, 20), list(range(10, 20)))
        self.assertEqual(myrange(10, 20, 3), list(range(10, 20, 3)))
        self.assertEqual(myrange(20, 10, -2), list(range(20, 10, -2)))
        #self.assertEqual(myrange(20, 10, 0), list(range(20, 10, 0)))


if __name__ == '__main__':
    unittest.main()
