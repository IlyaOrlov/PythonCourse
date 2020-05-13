class NonValidInput(Exception):
    pass

def to_roman(num):
    a = {'1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX'}
    b = {'1': 'X', '2': 'XX', '3': 'XXX', '4': 'XL', '5': 'L', '6': 'LX', '7': 'LXX', '8': 'LXXX', '9': 'XC'}
    c = {'1': 'C', '2': 'CC', '3': 'CCC', '4': 'CD', '5': 'D', '6': 'DC', '7': 'DCC', '8': 'DCCC', '9': 'CM'}
    f = {'1': 'M', '2': 'MM', '3': 'MMM', '4': 'MV', '5': 'V'}
    s = ''
    if isinstance(num, int) and 1 <= num <= 5000:
        num = str(num)
        if len(num) == 1:
            return a[num]
        elif len(num) == 2:
            s = b[num[0]] + a[num[1]]
        elif len(num) == 3:
            s = c[num[0]] + b[num[1]] + a[num[2]]
        elif len(num) == 4:
            s = f[num[0]] + c[num[1]] + b[num[2]] + a[num[3]]
    else:
        raise NonValidInput
    return s

print(to_roman(int(input(''))))

