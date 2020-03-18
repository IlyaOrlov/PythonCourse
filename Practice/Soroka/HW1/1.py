def big(a, b):
    if a > b:
        print(a)
    elif a == b:
        print('These numbers are equal')
    else:
        print(b)

big(5, 7)
big(8,100)
big(7, 7)

print(' ')

a = int(input('Input any number:'))
b = int(input('Input another number:'))
print(max(a, b))

print(' ')

def big2(x,y):
    if x > y:
        return x
    elif x == y:
        print('They are equal, genius!', end=' ')
        return x
    return y

print(big2(5,7))
print(big2(123,77))
print(big2(55,55))
print(big2(-86,33))
