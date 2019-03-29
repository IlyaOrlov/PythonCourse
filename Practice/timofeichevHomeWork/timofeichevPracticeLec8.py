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
        s.append(l[-1])
        del l[-1]
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
        if b[i - 1] == ' ' or i == 0:
            b[i] = b[i].upper()
        i = i + 1
    c = ''.join(b)
    return(c)
print(to_title(a))


a = 'привет, дорогой друг'
def to_title(a):
    b = a.split()
    i = 0
    while i < len(b):
        b[i] = b[i].capitalize()
        i = i + 1
    c = ' '.join(b)
    return(c)
print(to_title(a))


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
    return('Символ встречается {} раза'.format(c))
print(count_symbol(a, b))


# Задание 7 Вариант 1

with open('source.txt', 'w') as f:
    f.write('1')
    z = 'source.txt'
with open('destination.txt', 'w') as f1:
    f1.write('2')
    l = 'destination.txt'
def myfile(z, l):
    try:
        with open(z) as f:
            a = f.read()
            print(a)
            anew = a
        with open('destination.txt', 'x') as f1:
            f1.write(anew)
            b = 'destination.txt'
        with open(b) as f2:
            c = f2.read()
            print(c)
    except FileNotFoundError:
        print('Такой файл не найден')
    except FileExistsError:
        print('Такой файл уже существует,запись невозмжна')
myfile(z, l)

# Вариант 2

import os.path

class MyError(Exception):
    pass

with open('source.txt', 'w') as f:
    f.write('1')
    a = 'source.txt'
def test(a):
    if not os.path.isfile(a):
        raise MyError()
try:
    test(a)
except MyError:
    print('Такой файл не найден')
else:
    with open(a) as f:
        b = f.read()
        print(b)

with open('destination.txt', 'w') as f1:
    f1.write('2')
    b = 'destination.txt'
def test1(b):
    if os.path.isfile(b) :
        raise MyError ()
try:
    test1(b)
except MyError:
    print('Такой файл уже существует,запись невозможна')
else:
    with open('destination.txt', 'w') as f1:
        f1.write('3')
        b = 'destination.txt'
    with open(b) as f1:
        c = f1.read()
        print(c)


# Задание 9 Вариант 1

class User:

    name = None
    age = None

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

class Worker(User):

    salary = None

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary

if __name__ == '__main__':
    a = Worker()
    a.setName('Bob')
    a.setAge(18)
    a.setSalary(2000)
    print(a.getName())
    print(a.getAge())
    print(a.getSalary())
    b = Worker()
    b.setName('Pit')
    b.setAge(19)
    b.setSalary(2500)
    print(b.getName())
    print(b.getAge())
    print(b.getSalary())
    print('Сумма зарплат равна:{}'.format(a.getSalary()+b.getSalary()))

# Вариант 2

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

class Worker(User):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def getSalary(self):
        return self.salary

if __name__ == '__main__':
    a = Worker('Bob', 18, 2000)
    print(a.getName())
    print(a.getAge())
    print(a.getSalary())
    b = Worker('Pit', 19, 2500)
    print(b.getName())
    print(b.getAge())
    print(b.getSalary())
    print('Сумма зарплат равна:{}'.format(a.getSalary()+b.getSalary()))
