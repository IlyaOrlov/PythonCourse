import time
import random
from lecture5_task1 import Man


class Pupil(Man):
    def __init__(self, name=""):
        super().__init__(name)

    def solve_task(self):
        t=random.randint(3, 6)
        time.sleep(t)
        return print ("{}: I'm not ready yet".format(self.name))


a=Pupil("Вяся")
a.solve_task()