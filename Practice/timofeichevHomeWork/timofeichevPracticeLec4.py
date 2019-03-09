# Задание №1

l = range(1, 101)

def test(l):
    for i in l:
        if i % 15 == 0:
            i = 'FizzBuzz'
        elif i % 3 == 0:
            i = 'Fizz'
        elif i % 5 == 0:
            i = 'Buzz'
        print(i, end = ',')
test(l)


# Задание №2

a = input('Введите 5-ти значное число:')
while a.isdigit():
    if len(a) == 5:
        c = 0
        for i in a:
            c += 1
            print('{} цифра равна {}'.format(c, i))
        break
    else:
        print('Вы ввели не 5-ти значное число')
        a = input('Введите 5-ти значное число:')
else:
    print("Вы ввели не число")


# Задание №3

# Рекурсия

s = [0, 3, 24, 2, 3, 7]
l = []
def test(s, l):
    if len(s) != 0:
        a = s.index(min(s))
        l.append(s[a])
        del s[a]
        test(s, l)
    else:
        print('Список отсортирован:{}'.format(l))
test(s, l)


# Цикл while

s = [0, 3, 24, 2, 3, 7]
l = []
def test(s, l):
    while len(s) != 0:
        a = s.index(min(s))
        l.append(s[a])
        del s[a]
    else:
        print('Список отсортирован:{}'.format(l))
test(s, l)


# Данную идею позаимствовал у Е.Федотовой.Но с разбором и пониманием.

arr = [0,3,24,2,3,7]
i = 0
while i < len(arr):
    m = i
    j = i + 1
    while j < len(arr):
        if arr[m] < arr[j]:
            j += 1
        else:
            m = j
            j += 1
    arr[i], arr[m] = arr[m], arr[i]
    i += 1
print(arr)


# Задание 4
# Строка

s = 'Ре ализовать\tфункци    ональ ноcть\tкоторая бы'

def test(s):
    if "\t" in s:
        s = s.replace("\t", "    ")
    elif "    " in s:
        s = s.replace("    ", "\t")
    print(s)
test(s)


import re

s = 'Ре ализовать\tфункци    ональ ноcть\tкоторая бы'

def test(s):
    if "\t" in s:
        s = re.sub("\t", "    ", s)
    elif "    " in s:
        s = re.sub("    ", "\t", s)
    print(s)
test(s)
