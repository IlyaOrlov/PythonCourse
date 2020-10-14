import time
import random
from lab5_1 import Man

class Pupil(Man):

    def solve_task(self):
        time.sleep(random.randint(3, 7))
        print("I'm ready now?")

man1 = Pupil("Masha")
man1.solve_task()
print(man1.name)
