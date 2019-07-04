from nose.tools import assert_equals, raises

class TestWithNose:
    def setup(self):
        print('Before test case')
    def teardown(self):
        print('After test case')
    @classmethod
    def setup_class(cls):
        print('Before test suite')
    @classmethod
    def teardown_class(cls):
        print('After test suite')
    def test_numbers_5_6(self):
        assert_equals(5 * 6, 30)
    def test_strings_b_2(self):
        assert_equals('b' * 2, 'bb')
    @raises(ZeroDivisionError)
    def test_zero_division(self):
        a = 10 / 0
