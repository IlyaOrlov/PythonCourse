from time import sleep
from random import randint


class Man:

    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print("I'm not ready yet")


class Pupil(Man):

    def solve_task(self):
        sleep(randint(3, 6))
        print("I'm not ready too")


example = Man('Ivan Ivanov')
print(example.name)
example.solve_task()

example1 = Pupil('Aleksey Alekseev')
print(example1.name)
example1.solve_task()
