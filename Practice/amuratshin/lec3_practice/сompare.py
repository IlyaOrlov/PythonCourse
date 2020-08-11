
numFirst = int(input('Введите первое число:'))
numSecond = int(input('Введите второе число:'))

def intMoreThan(numFirst, numSecond):
    """ функция сравнивает два числа"""
    if numFirst < numSecond:
        print(numSecond)
    elif numFirst > numSecond:
        print(numFirst)
    else:
        print(' Числа равны')

intMoreThan()
