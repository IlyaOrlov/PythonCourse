import time
import random

class Man:
    def __init__(self, name):
        self.name = name
    def solve_task(self):
        print("Hold on!")

class Pupil(Man):
    def solve_task(self):
        time.sleep(random.randint(3, 6))
        print("I'm not ready yet")

n = Man('')
n.solve_task()
p = Pupil('')
p.solve_task()

