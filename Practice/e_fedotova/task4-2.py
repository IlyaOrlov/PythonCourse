num = input('Введите пятизначное число: ')

if len(num) == 5:
    print(num, "состоит из:")
    i = 1
    for i, item in enumerate(num):
        print(i+1, "цифра - это", num[i])
else:
    print("Число должно быть пятизначным")