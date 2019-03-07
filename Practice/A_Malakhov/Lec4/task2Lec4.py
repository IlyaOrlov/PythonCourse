a = int(input())
while a:
    a1 = str(a)
    if 10000 <= a < 100000:
        print('число:', a1)
        print('1 цифра равна', a1[0])
        print('2 цифра равна', a1[1])
        print('3 цифра равна', a1[2])
        print('4 цифра равна', a1[3])
        print('5 цифра равна', a1[4])
        break
    elif a < 0:
        print('Введите неотрицательное число!')
        a = int(input())
    else:
        print('Нужно ввести пятизначное число!')
        a = int(input())
