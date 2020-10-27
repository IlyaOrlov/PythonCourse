import time
import random
from Lection_5_Task_1 import Man


class Pupil(Man):
    def __init__(self, name):
        super(Pupil, self).__init__(name)

    def solve_task(self):
        time.sleep(random.randint(3, 7))
        print("I'm ready now?")


Jak = Pupil("Vopel")
Jak.solve_task()
print(Jak.name)
