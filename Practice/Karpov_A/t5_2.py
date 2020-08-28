import time
import random

class Man:
    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print("I'm not ready yet")

Tom = Man('Tom')
print(Tom.solve_task())

class Pupil(Man):
    def solve_task(self):
        time.sleep(random.randint(3,6))
        print("I'm not ready yet")

Tom = Pupil('Tom')
print(Tom.solve_task())
