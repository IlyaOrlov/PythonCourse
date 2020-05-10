class NonValidInput(Exception):
    pass


def to_roman(number):
    if isinstance(number, int) and 1 <= number <= 5000:
        result = ''
        for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                                 'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
            result += number // arabic * roman
            number %= arabic
        return result
    else:
        raise NonValidInput()
