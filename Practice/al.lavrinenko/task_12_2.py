class NonValidInput(Exception):
    pass


def to_roman(number):
    if not isinstance(number, int) or not 5000 > number > 0:
        raise NonValidInput
    roman_output = []
    for arabic, roman in ((1000, 'M'),
                          (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
                          (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
                          (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')):
        roman_output.append(number // arabic * roman)
        number %= arabic
    return ''.join(roman_output)
