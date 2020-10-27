from lec5task1 import Man
import time
import random

class Pupil (Man):
    def __init__(self, name):
        super().__init__(name)

    def solve_task(self):
        time.sleep(random.randint(3,6))
        print("I'm not ready yet")

p = Pupil("Jack")
p.solve_task()