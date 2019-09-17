def number_5():
    """Выводит пятизначное число познаково"""
    print('ввидите пятизначное число')
    number = str(input())
    if len(number) == 5:
        for i in range(len(number)):
            print('{} цифра равна {}'.format(i+1, number[i]))
    else:
        print('введенное число больше или меньше 5 знаков')


number_5()