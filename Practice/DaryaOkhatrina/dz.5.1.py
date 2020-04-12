import time
import random as r


class Man:
    def __init__(self, name):
        self.name = name
    def solve_task(self):
        print(self.name, "I'm not ready yet")

class Pupil(Man):
    def solve_task(self):
        time.sleep(r.randint(3, 6))
        print(self.name, "I'm not ready yet")



x = Man('Ivan')
x.solve_task()
y = Pupil('Sasha')
y.solve_task()
