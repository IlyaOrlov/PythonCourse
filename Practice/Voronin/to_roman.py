class NonValidInput(Exception):
    pass

def to_roman(num):
    a = {'0': '', '1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX'}
    b = {'0': '', '1': 'X', '2': 'XX', '3': 'XXX', '4': 'XL', '5': 'L', '6': 'LX', '7': 'LXX', '8': 'LXXX', '9': 'XC'}
    c = {'0': '', '1': 'C', '2': 'CC', '3': 'CCC', '4': 'CD', '5': 'D', '6': 'DC', '7': 'DCC', '8': 'DCCC', '9': 'CM'}
    f = {'0': '', '1': 'M', '2': 'MM', '3': 'MMM', '4': 'MV', '5': 'V'}
    s = ''
    lst = [a, b, c, f]
    if isinstance(num, int) and 1 <= num <= 5000:
        num = str(num)[::-1]
        for i in range(len(num)):
            s = lst[i][num[i]] + s
    else:
        raise NonValidInput
    return s

if __name__ == '__main__':
    print(to_roman(int(input(''))))

