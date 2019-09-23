# Task 1

class Man:
    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print('I`m not ready yet')

j = Man('John')
j.solve_task()
print(j.name)

# Task 2

import random
import time

class Man:
    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print('I`m not ready yet')

class Pupil(Man):

    def __init__(self, name):
        super().__init__(name)

    def solve_task(self):
        num = random.randint(3, 6)
        time.sleep(num)
        return print('I`m not ready yet')

c = Pupil('Frank')
print(c.name)
c.solve_task()