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

    for char in str:
        print("1 цифра равна {}".format(char))


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
    count = -1
    arr = [
        [1, 2, 37, 98, 5],
        [3, 72, 9, 19, 7],
        [12, 10, 8, 4, 0],
        [13, 14, 35, 40, 11],
        [30, 89, 78, 45, 65]
    ]

    while i < len(arr):
        while j < len(arr[i]):
            if arr[i][j] == int(num):
                count = j
                print(count)
            j += 1
        i += 1
        j = 0
    i = 0
    if count != -1:
        while i < len(arr):
            while j < len(arr[i]):
                if j == count:
                    del arr[i][j]
                j += 1
            j = 0
            i += 1
    print(arr)


zad6()
