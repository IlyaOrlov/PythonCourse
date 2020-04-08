x = input('Введите пятизначное число: ')
while len(str(x)) != 5 or x.isdigit() is False:
    print('Не получилось! Попробуйте ещё!).')
    x = input('Введите пятизначное число: ')
else:
    v = 1
    for i in str(x):
        print(v, 'цифра равна', i)
        v += 1
