from random import randint
from time import sleep


class Man:

    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print('Hello! I am', self.name, 'I am not ready yet')


class Pupil(Man):
    def __init__(self, name):
        super().__init__(name)

    def solve_task(self):
        t = randint(3, 6)
        print('I am thinking...')
        sleep(t)
        print('Hello! I am', self.name, 'I am not ready yet')


Bill = Man('Bill')
Bill.solve_task()
Bob = Pupil('Bob')
Bob.solve_task()
