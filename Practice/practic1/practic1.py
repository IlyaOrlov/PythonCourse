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

    for char in str:
        print("{} цифра равна {}".format(index, char))
        index +=1


zad2()


def zad3():
    i = 0
    arr = [0, 3, 24, 2, 3, 7]

    while i < len(arr):
        # находим минимальный элемент
        s = arr[i:]
        x = min(s)
        # индекс минимального элемента
        j = arr.index(x, i)
        # сохраняем значение i-ого элемента
        num = arr[i]
        # заменяем i-ый элемнт на минимальное значение
        arr[i] = x
        # заменяем минимальный элемент i-ым
        arr[j] = num
        i += 1
    print(arr)


zad3()


def zad4():
    string = "Привет    это моя первая  строка  !"
    str1 = "    "
    str2 = "\t"
    if string.find(str1) != -1:
        s = string.replace(str1, str2)
    if string.find(str2) != -1:
        s = string.expandtabs(4)
    print(s)


zad4()


def zad6():
    num = input("Enter the number: ")
    i = 0
    j = 0
    arr = [
        [1, 56, 37, 98, 5],
        [3, 45, 9, 27, 25],
        [12, 10, 8, 4, 89],
        [24, 2, 2, 2, 2],
        [30, 89, 78, 45, 65]
    ]

    # Новый вариант

    while j < len(arr[i]):
        while i < len(arr):
            if arr[i][j] == int(num):
                k = 0
                while k < len(arr):
                    del arr[k][j]
                    k += 1
                j = 0
                i = 0
            i += 1
        i = 0
        j += 1

    # Старый вариант

    # while i < len(arr):
    #     while j < len(arr[i]):
    #         if arr[i][j] == int(num):
    #             count = j
    #             print(count)
    #         j += 1
    #     i += 1
    #     j = 0
    # i = 0
    # if count != None:
    #     while i < len(arr):
    #         while j < len(arr[i]):
    #             if j == count:
    #                 del arr[i][j]
    #             j += 1
    #         j = 0
    #         i += 1
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
