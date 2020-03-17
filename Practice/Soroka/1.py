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

#если переменную получаем от пользователя:
a = int(input('Input any number:'))
b = int(input('Input another number:'))

if a > b:
    print('A bigger number is', (a))
elif a == b:
    print('The numbers are equal')
else:
    print('A bigger number is', (b))

#здесь так же можно заменить else на:
#elif a < b:
    #print ('A bigger number is', (b))
#но это чуть длиннее

print(' ')

def big(x,y):
    if x > y:
        return(x)
    elif x == y:
        print('They are equal, genius!', end=' ')
        return(x, y)
    return(y)

print(big(5,7))
print(big(123,77))
print(big(55,55))
print(big(-86,33))