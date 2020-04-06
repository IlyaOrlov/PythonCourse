class Man:
    def __init__(self, name):
        self.name = name
    def solve_task(self):
        print("I'm not ready yet")

Serg = Man('Serg')
print(Serg.solve_task())

import random
import time

class Pupil(Man):
    def solve_task(self):
        time.sleep(random.randint(3,6))
        print("I'm not ready yet")

Serg = Pupil('Serg')
print(Serg.solve_task())