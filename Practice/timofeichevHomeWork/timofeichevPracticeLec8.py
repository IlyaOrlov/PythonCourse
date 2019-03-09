# Задание 1

l = [1, 2, 3, 4, 5]
def test(l):
    c = 0
    for i in l:
        c = c + 1
    return('Длина списка равна:{}'.format(c))
print(test(l))


# Задание 2

l = [1, 2, 3, 4, 5]
s = []
def test(l, s):
    while len(l) != 0:
        a = l.index(l[-1])
        s.append(l[a])
        del l[a]
    else:
        print('Список отсортирован:{}'.format(s))
test(l, s)


l = [1, 2, 3, 4, 5]
def test(l):
    c = 0
    while c < len(l) / 2:
        l[c], l[-c - 1] = l[-c - 1], l[c]
        c = c + 1
    else:
        print('Список отсортирован:{}'.format(l))
test(l)


# Задание 4

a = 'привет, дорогой друг'
def to_title(a):
    b = list(a)
    i = 0
    while i < len(b):
        if b[i - 1] == ' ':
            b[i] = b[i].upper()
        elif b[0]:
            b[0] = b[0].upper()
        i = i + 1
    c = ''.join(b)
    print(c)
to_title(a)


a = 'привет, дорогой друг'
def to_title(a):
    b = a.split()
    i = 0
    while i < len(b):
        b[i] = b[i].capitalize()
        i = i + 1
    c = ' '.join(b)
    print(c)
to_title(a)


a = 'привет, дорогой друг'
def to_title(a):
    b = a.split()
    for i in b:
        i = i.capitalize()
        print(i, end = ' ')
to_title(a)


# Задание 5

a = 'Тимофеичев Андрей'
b = 'е'
def count_symbol(a, b):
    c = 0
    for i in a:
        if i == b:
            c = c + 1
    print('Символ встречается {} раза'.format(c))
count_symbol(a, b)
