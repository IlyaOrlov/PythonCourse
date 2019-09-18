def fun(data):
    for i in range(len(data)):
        print("{} цифра равна {}". format(i+1, data[i]))


res = input("Введите пятизначное число: ")
if res.isdigit():
    if int(res)<=10000:
        print("Число должно быть пятизначным")
    else:
        fun(res)
else:
    print ('Необходимо ввести число, а не строку')



