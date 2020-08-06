#сравнить два числа

def intMoreThan():
    numFirst = int(input('Введите первое число:'))
    numSecond = int(input('Введите второе число:'))
    if numFirst < numSecond:
        print(numSecond)
    elif numFirst > numSecond:
        print(numFirst)
    else:
        print(' Числа равны')

intMoreThan()
