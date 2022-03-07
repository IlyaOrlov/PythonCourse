# Написать и вызвать функцию,принимающую два числа и выводящую на экран большее из двух.
def print_num(a, b):
    if a > b:
        print(a)
    else:
        print(b)


print_num(9, 10)


# Написать и вызвать функцию,принимающую два числа и возвращающую большее из двух.
def return_num(a, b):
    return a if a > b else b


print(return_num(14, 15))
