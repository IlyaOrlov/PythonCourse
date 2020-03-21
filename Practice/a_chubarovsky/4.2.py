a = input('Введите пятизначное число: ')

print('Число: {}'.format(a))
lst1 = list(a)
if len(lst1) == 5:
    i = 0
    while i <= len(lst1):
        print("{} цифра равна {}".format((i + 1), lst1[i]))
        i += 1
else:
    print('Введённое число не пятизначное.')
