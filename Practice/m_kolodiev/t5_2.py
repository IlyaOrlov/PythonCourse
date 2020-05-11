import time
import random
from t5_1 import Man


class Pupil(Man):
    def __init__(self, name):
        super().__init__(name)

    def solve_task(self):
        t = random.randint(3, 6)
        print("Waiting for {} seconds".format(t))
        time.sleep(t)
        print("I'm not ready yet.")


b = Pupil('Frankie')
print(b.name)
b.solve_task()
