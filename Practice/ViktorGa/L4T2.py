def read_number(number):
    numbers = str(number)
    for num, val in enumerate(numbers, 1):
        print(str(num) + ' цифра = ' + str(val))
    return True


read_number(10819)