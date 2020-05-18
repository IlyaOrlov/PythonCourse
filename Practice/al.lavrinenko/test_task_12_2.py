from nose.tools import assert_equals, raises
from task_12_2 import to_roman, NonValidInput


class TestToRoman:
    def test_normal(self):
        assert_equals(to_roman(4999), 'MMMMCMXCIX')
        assert_equals(to_roman(3876), 'MMMDCCCLXXVI')

    @raises(NonValidInput)
    def test_NonValidInput1(self):
        to_roman(0)

    @raises(NonValidInput)
    def test_NonValidInput2(self):
        to_roman(5000)

    @raises(NonValidInput)
    def test_NonValidInput3(self):
        to_roman(10.39)
