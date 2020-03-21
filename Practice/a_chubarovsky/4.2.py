a = input('Введите пятизначное число: ')

print('Число: {}'.format(a))
lst1 = list(a)
if len(lst1) == 5:
    for i in lst1:
        print("{} цифра равна {}".format((lst1.index(i) + 1), i))
else:
    print('Введённое число не пятизначное.')
