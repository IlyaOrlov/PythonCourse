def func_return(value1, value2):
    if value1 >= value2:
        return value1
    else:
        return value2


a = int(input('введите первое число: '))
b = int(input('введите второе число: '))

print(func_return(a, b))


