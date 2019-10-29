class NonValidInput(Exception):
    def __init__(self):
        super().__init__('Non Valid Input. Please enter an integer between 1 and 5000')


def to_roman(dec_number):
    if not isinstance(dec_number, int) or dec_number >= 5000 or dec_number < 1:
        raise NonValidInput
    rom_number = ''
    number = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
              5: 'V', 4: 'IV', 1: 'I'}
    for key in number:
        if dec_number // key > 0:
            rom_number += number[key] * (dec_number // key)
            dec_number -= key * (dec_number // key)
    return rom_number

