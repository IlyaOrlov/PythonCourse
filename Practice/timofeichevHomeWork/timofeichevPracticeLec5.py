# Разминка 2

a = [10, 20, 30, 40]
def test(a):
    b = 0
    for i in a:
        print('({}, {})'.format(b, i))
        b = b+1
test(a)


# Задание 1

class Man:
    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print('I am not ready yet')


a = Man('Timur')
a.solve_task()


# Задание 2

import time
import random

class Pupil(Man):
    def solve_task(self):
        time.sleep(random.randint(3, 6))
        print('I am not ready yet')


b = Pupil('Timur')
b.solve_task()


# Задание 1 (Вариант 2)

class Man1:
    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print('{},i am not ready yet'.format(self.name))


a = Man1('Timur')
a.solve_task()


# Задание 2 (Вариант 2)

class Pupil(Man1):
    def solve_task(self):
        time.sleep(random.randint(3, 6))
        print('{},i am not ready yet'.format(self.name))


b = Pupil('Timur')
b.solve_task()
