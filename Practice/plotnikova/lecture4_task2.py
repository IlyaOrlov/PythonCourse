def fun(data):
    for i in range(len(data)):
        print("{} цифра равна {}". format(i+1, data[i]))


res = input("Введите пятизначное число: ")
if res.isdigit():
    if len(res)==5:
        if int(res)<=10000:
            print("Число должно быть пятизначным")
        else:
            fun(res)
    else:
        print("Число должно быть пятизначным")
else:
    print ('Необходимо ввести число, а не строку')



