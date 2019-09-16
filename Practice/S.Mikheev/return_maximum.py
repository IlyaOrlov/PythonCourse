def maximum(a, b):
    return a if a > b else b
    # если a == b, то в любом случае будет выведено максимальное число


a = int(input('enter the first integer: '))
b = int(input('enter the second integer: '))
print('The maximum number is {}'.format(maximum(a, b)))

# можно использовать float вместо int для того,
# чтобы сравнивать числа с плавающей точкой