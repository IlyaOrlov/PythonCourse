while True:
    n = input("Введите пятизначное число: ")
    if n.isdigit() == 0:
        print("Ошибка введите ещё раз")
    elif len(n) != 5:
        print("Ошибка введите ещё раз")
    elif n[0] == '0':
        print("Ошибка введите ещё раз")
    else:
        break

for i in range(len(n)):
    print("{} число равно {}".format(i+1, n[i]))