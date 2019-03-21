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
def spisok(s, l):
    if len(s) != 0:
        a = s.index(min(s))
        l.append(s[a])
        del s[a]
        spisok(s, l)
    else:
        print('Список отсортирован:{}'.format(l))
spisok(s, l)


# Цикл while

s = [0, 3, 24, 2, 3, 7]
l = []
def spisok2(s, l):
    while len(s) != 0:
        a = s.index(min(s))
        l.append(s[a])
        del s[a]
    else:
        print('Список отсортирован:{}'.format(l))
spisok2(s, l)


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

def test1(s):
    if "\t" in s:
        s = s.replace("\t", "    ")
    elif "    " in s:
        s = s.replace("    ", "\t")
    print(s)
test1(s)


import re

s = 'Ре ализовать\tфункци    ональ ноcть\tкоторая бы'

def test_re(s):
    if "\t" in s:
        s = re.sub("\t", "    ", s)
    elif "    " in s:
        s = re.sub("    ", "\t", s)
    print(s)
test_re(s)


# Файл Вариант 1

f = open('1.txt', 'w')
f.write('Ре ализовать\tфункци    ональ ноcть\tкоторая бы')
f.close()
def file():
    a = open('1.txt')
    b = a.read()
    print(b)
    if '\t' in b:
        bnew = b.replace('\t', '    ')
    elif '    ' in b:
        bnew = b.replace('    ', '\t')
    h = open('2.txt', 'w')
    h.write(bnew)
    h.close()
    g = open('2.txt')
    k = g.read()
    print(k)
    g.close()
file()


# Файл Вариант 2 (Менеджер контекста)

with open('3.txt', 'w') as f:
    f.write('Ре ализовать\tфункци    ональ ноcть\tкоторая бы')

def file2():
    with open('3.txt') as f:
        b = f.read()
        print(b)
        if '\t' in b:
            bnew = b.replace('\t', '    ')
        elif '    ' in b:
            bnew = b.replace('    ', '\t')
        with open('4.txt', 'w') as z:
            z.write(bnew)
        with open('4.txt') as z:
            c = z.read()
            print(c)
file2()


# Задание 5

d = {1:"one", 2:'two', 3:"three"}
l = "I have 1 cat and 2 dog"

def slovar(d, l):
    if 1 in d:
        l = l.replace('1', d[1])
    if 2 in d:
        l = l.replace('2', d[2])
    return l
print(slovar(d, l))


# Задание 6
# Вариант 1

M = [[8, 2, 3], [4, 4, 6], [7, 11, 5]]
a = int(input('Введите число:'))
def array(M, a):
    for i in M:
        for m in i:
            if a == m:
                c = i.index(a)
                for i in M:
                    del i[c]
                array(M, a)
                return M
print(array(M, a))


# Вариант 2

M = [[8, 2, 3], [4, 4, 6], [7, 11, 5]]
a = int(input('Введите число:'))

def array2(M, a):
    result = [[row[i] for row in M] for i in range(len(M[0]))]
    edited = [result[j] for j in range(len(result)) if a not in result[j]]
    finish = [[row[i] for row in edited] for i in range(len(edited[0]))]
    return finish
print(array2(M, a))

