def big(a, b):
    if a > b:
        print(a)
    elif a == b:
        print('These numbers are equal')
    else:
        print(b)

big(5, 7)
big(8, 100)
big(7, 7)
big(int(input('Введи число:')), int(input('Введи другое число:')))

print(' ')

def big2(x, y):
    if x > y:
        return x
    elif x == y:
        print('They are equal, genius!', end=' ')
        return x
    return y

print(big2(5, 7))
print(big2(123, 77))
print(big2(55, 55))
print(big2(-86, 33))
print(big2(int(input('Введи число:')), int(input('Введи другое число:'))))

