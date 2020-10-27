class NonValidInput(Exception):
    pass


def to_roman(number):
    roman_dict = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'XI',
                  10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC',
                  100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM',
                  1000: 'M', 2000: 'MM', 3000: 'MMM', 4000: 'M\u2181', 5000: '\u2181'}
    if number < 1 or number > 5000:
        raise NonValidInput("Number: '{}' is out of range from 1 to 5000".format(number))
    if number % 1000 == 0:
        return roman_dict[number]
    rom_thousands = ''
    rom_hundreds = ''
    rom_decades = ''
    rom_unit = ''
    number_str = str(number)
    length = len(number_str)
    for digit in number_str:
        digit = int(digit)
        if length == 4:
            thousands = digit * 1000
            rom_thousands = roman_dict[thousands]
        elif length == 3:
            hundreds = digit * 100
            rom_hundreds = roman_dict[hundreds]
        elif length == 2:
            decades = digit * 10
            rom_decades = roman_dict[decades]
        elif length == 1:
            unit = digit
            rom_unit = roman_dict[unit]
        length -= 1
    return f'{rom_thousands}{rom_hundreds}{rom_decades}{rom_unit}'
