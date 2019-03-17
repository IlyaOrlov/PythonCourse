import time
import random


class Pupil:
    def __init__(self, name):
        self.name = name

    def solve_task(self):
        time.sleep(random.randint(3, 6))
        print("I'm not ready yet!")


y = Pupil('Andrew')
y.solve_task()



