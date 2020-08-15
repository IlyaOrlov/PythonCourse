# Составить программу, которая будет считывать введённое пятизначное число.
# После чего, каждую цифру этого числа необходимо вывести в новой строке:

def read_number(number):
    if not str(number).isdigit():
        print("incorrect input")
        return False
    numbers = str(number)
    for num, val in enumerate(numbers, 1):
        print(str(num) + ' цифра равна ' + str(val))
    return True


read_number(10819)
