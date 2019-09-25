import time
import random

class Man():

    def __init__(self, name=""):
        self.name=name
        # self.solve_task()

    def solve_task(self):
        return print ("I'm not ready yet")


class Pupil(Man):
    def __init__(self, name=""):
        super().__init__(name)

    def solve_task(self):
        t=random.randint(3, 6)
        time.sleep(t)
        return print ("I'm not ready yet")


a=Pupil()
a.solve_task()