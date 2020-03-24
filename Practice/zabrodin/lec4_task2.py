x = int(input('Введите пятизначное число: '))
while len(str(x)) != 5:
    print('Число не пятизначное! Попробуйте ещё!')
    x = int(input('Введите пятизначное число: '))
else:
    v = 1
    for i in str(x):
        print(v, 'цифра равна', i)
        v += 1

