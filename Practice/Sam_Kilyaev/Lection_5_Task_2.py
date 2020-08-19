import time
import random


class Man(object):
    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print("I'm not ready yet")


class Pupil(Man):
    def __init__(self, name):
        super(Pupil, self).__init__(name)

    def solve_task(self):
        time.sleep(random.randint(3, 7))
        print("I'm ready now?")


Jak = Pupil("Vopel")
Jak.solve_task()
print(Jak.name)