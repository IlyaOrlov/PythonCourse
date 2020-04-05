import random as rdm
import time
from 5.1 import Man


class Pupil(Man):
    def solve_task(self):
        time.sleep(rdm.randint(3, 6))
        print("{} says: I'm not ready yet.".format(self.name))

        
m = Man('Misha')
print(m.solve_task())
p = Pupil('Ivan')
print(p.solve_task())
