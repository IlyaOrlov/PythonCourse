class NonValidInput(Exception):
    pass


rom = {'1': 'I', '5': 'V', '10': 'X', '50': 'L', '100': 'C', '500': 'D', '1000': 'M', '5000': 'U'}


def to_roman(number):
    if 0 > number or number > 5000:
        raise NonValidInput('number out of range (5000)')
    result = []
    length = len(str(number))
    for i in str(number):
        num = int(i) * 10**(length-1)
        if 0 <= num - 5 * 10**(length-1) <= 3*10**(length-1):
            result.append(rom[str(5 * 10**(length-1))])
            num -= 5 * 10**(length-1)
        elif num - 5 * 10**(length-1) > 3*10**(length-1):
            result.append(rom[str(10 ** (length - 1))])
            if 5 * 10**(length-1) - num > 0:
                result.append(rom[str(5*10**(length-1))])
            else:
                result.append(rom[str(10**(length))])
            num -= 10 ** (length)
        elif -10**(length-1) <= num - 5 * 10**(length-1) <= 0:
            result.append(rom[str(10 ** (length - 1))])
            if 5 * 10 ** (length - 1) - num > 0:
                result.append(rom[str(5 * 10 ** (length - 1))])
            else:
                result.append(rom[str(10**length)])
            num -= 5 * 10**(length-1)
        if num - 10**(length-1) >= 0:
            n = num // 10**(length-1)
            for _ in range(n):
                result.append(rom[str(10**(length-1))])
                num -= 10 ** (length - 1)
        length -= 1
    return ''.join(result)
