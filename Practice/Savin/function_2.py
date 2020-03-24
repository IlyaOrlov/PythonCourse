a = int(input('введите a: '))
b = int(input('введите b: '))


def greater(a, b):
    if a > b:
        return a
    else:
        return b


print(greater(a, b))
