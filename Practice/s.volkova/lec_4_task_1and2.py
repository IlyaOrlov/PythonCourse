#for Python 3.6
#Classes tasks 1 and 2

from time import sleep
from random import randint

class Human:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def solve_task():
        print("I'm not ready yet")

class Pupil(Human):
    
    @staticmethod
    def solve_task():
        sleep(randint(3,6))
        print("I'm not ready yet")


if __name__ == '__main__':
    Mary = Human("Mary Jane")
    Tony = Pupil("Anthony Cole")
    print(Mary.name)
    Mary.solve_task()
    print(Tony.name) 
    Tony.solve_task()
