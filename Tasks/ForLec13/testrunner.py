import unittest

testmodules= [
    'test_string_methods',
    'test_skip'
]


if __name__ == '__main__':
    suite = unittest.TestSuite()
    for tm in testmodules:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(tm))
    unittest.TextTestRunner().run(suite)