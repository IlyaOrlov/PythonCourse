num = input('Введите пятизначное число: ')

if len(num) == 5:
    print(num, "состоит из:")
    l = num
    i = 1
    for i, item in enumerate(l):
        print(i+1, "цифра - это", l[i])
else:
    print("Число должно быть пятизначным")