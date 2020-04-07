import time
import random

class fun:
    def __init__(self,name):
        self.value=name

    def solve_task(self):
        print("I'm not ready yet")

class Pupil(fun):
    def solve_task(self):
        self.t=random.randint(3,6)
        print("I will be ready in {} sec".format(self.t))
        self.sec=time.sleep(self.t)
        print("I'm ready")

f=Pupil("J.")
f.solve_task()
