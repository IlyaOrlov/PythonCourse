#1 Написать и вызвать функцию, принимающую два числа и выводящую на экран большее из двух.
def fun_print_max(num1, num2):
    if num1 > num2:
        print(f"Max number is {num1}")
    else:
        print(f"Max number is {num2}")

fun_print_max(15, -5)


#2 Написать и вызвать функцию, принимающую два числа и возвращающую большее из двух
def fun_return_max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

check = fun_return_max(0, -1)
print (f"Max number is {check}")