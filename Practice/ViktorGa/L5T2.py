from random import randint
from time import sleep


class Man:
    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print("I'm not ready yet")


class Pupil(Man):
    def solve_task(self):
        print("thinking...")
        time = randint(3, 6)
        sleep(time)
        print("I'm ready")


man = Man("karlson")
man.solve_task()
pupil = Pupil("malysh")
pupil.solve_task()