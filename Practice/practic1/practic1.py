def zad1():
    i = 0

    while i <= 100:
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
        i += 1


zad1()


def zad2():
    str = input("Введите число: ")
    index = 0

    if len(str) == 5:
        for char in str:
            print("{} цифра равна {}".format(index, char))
            index +=1
    else:
        print("Not five-digit number!")

zad2()


def zad3():
    i = 0
    arr = [0, 3, 24, 2, 3, 7]

    while i < len(arr):
        # находим минимальный элемент
        x = min(arr[i:])
        # индекс минимального элемента
        j = arr.index(x, i)
        arr[i], arr[j] = x, arr[i]
        i += 1
    print(arr)


zad3()


def zad4():
    string = "Привет    это моя первая  строка  !"
    str1 = "    "
    str2 = "\t"
    if string.find(str1) != -1:
        s = string.replace(str1, str2)
    else:
        s = string.expandtabs(4)
    print(s)


zad4()


def zad6():
    num = input("Enter the number: ")
    check = 0
    i = 0
    j = 0
    arr = [
        [1, 56, 37, 98, 5],
        [3, 45, 9, 27, 25],
        [12, 10, 8, 4, 89],
        [2, 2, 2, 2, 2],
        [30, 89, 78, 45, 65]
    ]

    if len(arr):
        while j < len(arr[i]):
            while i < len(arr):
                if len(arr[i]) != 0 and arr[i][j] == int(num):
                    check = 1
                    k = 0
                    while k < len(arr):
                        del arr[k][j]
                        k += 1
                    j = 0
                    # i = 0
                if check == 1:
                    i = 0
                    check = 0
                else:
                    i += 1

            i = 0
            j += 1
    print(arr)


zad6()

def zad5():
    string = "одна голова - хорошо, а две - лучше"
    dct = {"одна": "1", "две": "2"}
    if string.find("одна") != -1:
        s = string.replace("одна", dct.get("одна"))
        if s.find("две") != 1:
            st = s.replace("две", dct.get("две"))
        else:
            st = s
    elif string.find("две") != -1:
        s = string.replace("две", dct.get("две"))
        if s.find("одна") != 1:
            st = s.replace("одна", dct.get("одна"))
        else:
            st = s
    print(st)

zad5()
