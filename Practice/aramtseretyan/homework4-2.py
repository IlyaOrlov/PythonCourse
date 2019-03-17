a = input('Введите 5-ти значное число:')


def Factorial(a):
    if len(a) == 5:
        b = 0
        for i in a:
            b += 1
            print('{} цифра равна {}'.format(b, i))
        else:
            print('Вы ввели не 5-ти значное число')
            a = input('Введите 5-ти значное число:'
    else:
         print("Вы ввели не число")


Factorial(a)
        



