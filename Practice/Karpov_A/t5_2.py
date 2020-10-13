import time
import random
from t5_1 import Man

class Pupil(Man):
    def __init__(self, name):
        self.name = name

    def solve_task(self):
        time.sleep(random.randint(3,6))
        print("I'm not ready ")

Tom = Pupil('Tom')
print(f"{Tom.name}:", end=" ")
Tom.solve_task()
