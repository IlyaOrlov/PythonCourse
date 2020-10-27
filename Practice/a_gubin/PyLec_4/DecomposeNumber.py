def decompose_from_string(str_number):
    for i, digit in enumerate(list(str_number.strip()), start=1):
        print(f"{i} цифра равна {digit}")


def decompose_from_number(int_number):
    digits = []
    base = 10
    while int_number:
        digits.insert(0, int_number % base)
        int_number //= base
    if not digits:
        digits.append(0)
    for i, digit in enumerate(digits, start=1):
        print(f"{i} цифра равна {digit}")


while True:
    str_number = input('Enter a number: ')
    try:
        int_number = int(str_number)
    except ValueError:
        print('Invalid format of number, please try again')
        continue
    break
decompose_from_string(str_number)
print('***************')
decompose_from_number(int_number)
