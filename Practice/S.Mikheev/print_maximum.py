def maximum(a, b):
    print('The maximum number is {}'.format(a if a > b else b))
    # если a == b, то в любом случае будет выведено максимальное число


maximum(int(input('enter the first integer: ')),
        int(input('enter the second integer: ')))

# можно использовать float вместо int для того,
# чтобы сравнивать числа с плавающей точкой
