import random
import time
class Man:

    def __init__(self, first_name):
        self.first_name = first_name

    def solve_task(self):
        print("{} say: I'm not ready yet".format(self.first_name))


class Pupil(Man):

    def solve_task(self):
        time.sleep(random.randint(3,6))
        print("{} say: I'm not ready yet".format(self.first_name))


Man = Man('Man')
print(Man.solve_task())
Pupil = Pupil('Pupil')
print(Pupil.solve_task())