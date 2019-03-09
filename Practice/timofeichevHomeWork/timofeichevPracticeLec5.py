# Разминка 2

a = [10, 20, 30, 40]
b = 0
def test(a, b):
    for i in a:
        print('({}, {})'.format(b, i))
        b = b+1
test(a, b)


# Задание 1

class Man:
    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print('I am not ready yet')


a = Man('Timur')
a.solve_task()


class Man1:
    def __init__(self):
         pass

    def solve_task(self, name):
        print('{},i am not ready yet'.format(name))


a = Man1()
a.solve_task('Timur')


# Задание 2

import time
import random

class Pupil(Man):
    def solve_task(self):
        time.sleep(random.randint(3, 6))
        print('I am not ready yet')


b = Pupil('Timur')
b.solve_task()


class Pupil(Man1):
    def solve_task(self, name):
        time.sleep(random.randint(3, 6))
        print('{},i am not ready yet'.format(name))


b = Pupil()
b.solve_task('Timur')
