perz = [1, 2, 3, 4, 5]
while True:
    print("Введите 5 значное число:")
    chislo = int(input())
    a = str(chislo)
    if len(a) == 5:
        i = 0
        while i < len(a):
            print("{} цифра равна:{}".format(perz[i],a[i]))
            i+=1
    else:
        print("Попробуй еще раз")


