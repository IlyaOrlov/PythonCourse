import random as rdm
import time

class Man:
    def __init__(self, name):
        self.name = name
    def solve_task(self):
        print("I'm not ready yet")

class Pupil(Man):
    def solve_task(self):
        time.sleep(rdm.randint(3, 6))
        print("I'm not ready yet")
a = Man('')
a.solve_task()
b = Pupil('')
b.solve_task()
