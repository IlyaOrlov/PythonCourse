from time import sleep
from random import randint

class Man:
    def __init__(self, name):
        self.name = name

    @classmethod
    def solve_task(cls):
        print("I'm not ready yet")

class Pupil(Man):
    def __init__(self, name):
        Man.__init__(self, name)

    @classmethod
    def solve_task(cls):
        sleep(randint(3, 6))
        print("I'm ready")

a = Man('Petr Petrov')
a.solve_task()

b = Pupil('Semen Semenov')
b.solve_task()
