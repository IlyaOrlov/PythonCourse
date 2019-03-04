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