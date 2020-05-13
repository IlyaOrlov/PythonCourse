class NonValidInput(Exception):
    pass

def to_roman(num):
    a = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
    b = {1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
    c = {1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}
    f = {1: 'M', 2: 'MM', 3: 'MMM', 4: 'MV', 5: 'V'}
    s = ''
    if isinstance(num, int) and 1 <= num <= 5000:
        num = str(num)
        if len(str(num)) == 1:
            return a[int(num)]
        elif len(str(num)) == 2:
            for i, x in enumerate(num):
                if int(x) > 0:
                    if i == 0:
                        s += b[int(x)]
                    elif i == 1:
                        s += a[int(x)]
        elif len(str(num)) == 3:
            for i,x in enumerate(num):
                if int(x) > 0:
                    if i == 0:
                        s += c[int(x)]
                    elif i == 1:
                        s += b[int(x)]
                    elif i == 2:
                        s += a[int(x)]
        elif len(str(num)) == 4:
            for i,x in enumerate(num):
                if int(x) > 0:
                    if i == 0:
                        s += f[int(x)]
                    elif i == 1:
                        s += c[int(x)]
                    elif i == 2:
                        s += b[int(x)]
                    elif i == 3:
                        s += a[int(x)]
    else:
        raise NonValidInput
    return s

# print(to_roman(int(input(''))))

