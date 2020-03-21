while True:
    print("Введите 5 значное число:")
    chislo =input()
    if chislo.isdigit():
        if len(chislo) == 5:
            i = 0
            while i < len(chislo):
                print("{} цифра равна:{}".format(i+1,chislo[i]))
                i+=1
        else:
            print("Попробуй еще раз")
    else:
        print("Число должно состоять из чисел")


