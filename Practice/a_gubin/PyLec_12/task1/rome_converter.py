

class NotValidInput(Exception):
    pass


romans_values = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}


def to_roman(digit):
    if not isinstance(digit, int):
        raise TypeError
    if not 1 <= digit <= 5000:
        raise NotValidInput()
    roman_digit = ""
    for value in romans_values:
        roman_digit += digit // value * romans_values[value]
        digit = digit % value
    return roman_digit
