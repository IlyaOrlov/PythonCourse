# Task 4.1
# Напишите программу, которая выводит на экран числа от 1 до 100.
# При этом вместо чисел, кратных трем, программа должна выводить слово Fizz, а вместо чисел, кратных пяти — слово Buzz.
# Если число кратно пятнадцати, то программа должна выводить слово FizzBuzz

def output_number():
    for i in range(1,101):
        if (i %3 == 0 and i %5 != 0):
            print ("Fizz")
        elif (i %5 == 0 and i %3 != 0):
            print("Buzz")
        elif (i %3 == 0 and i %5 == 0):
            print("FizzBuzz")
        else:
            print(i)

output_number()
