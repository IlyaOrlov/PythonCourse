# Напишите программу,которая выводит на экран числа от 1 до 100.
# При этом вместо чисел,кратных трем,программа должна выводить слово Fizz,
# а вместо чисел,кратных пяти — слово Buzz.
# Если число кратно пятнадцати,то программа должна выводить слово FizzBuzz.

def print_FizzBuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fizz")
        if i % 5 == 0:
            print("Buzz")
        if i % 15 == 0:
            print("FizzBuzz")
        else:
            print(i)


print(print_FizzBuzz())
