class Man:

    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print("I'm not ready yet")

m1 = Man("John")
print(m1.name)
m1.solve_task()

import time
import random

class Pupil(Man):

    def solve_task(self):
        time.sleep(random.randint(3, 6))
        print("I'm not ready yet")

p1 = Pupil("Kate")
print(p1.name)
p1.solve_task()