import time
import random


class Man:
    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print("I'm not ready yet")


class Pupil(Man):
    def solve_task(self):
        time.sleep(random.randint(3, 6))
        print("I'm not ready yet")


man1 = Pupil('Andrey')
print(man1.name)
man1.solve_task()
