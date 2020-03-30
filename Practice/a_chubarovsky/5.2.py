import random as rdm
import time


class Man:
    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print("{} says: I'm not ready yet.".format(self.name))


class Pupil(Man):
    def solve_task(self):
        time.sleep(rdm.randint(3, 6))
        print("{} says: I'm not ready yet.".format(self.name))
