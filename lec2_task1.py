def max_number(a, b):
    if a > b:
        print(a)
    elif a == b:
        print('числа равны')
    else:
        print(b)


x = int(input('введите первое число: '))
y = int(input('введите второе число: '))

max_number(x, y)
