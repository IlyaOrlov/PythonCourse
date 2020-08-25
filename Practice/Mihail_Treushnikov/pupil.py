import random
from time import sleep
from man import Man

class Pupil(Man):

    def __init__(self, name):
        super().__init__(name)

    def solve_task(self):
        sleep(random.randint(3,6))
        super(Pupil, self).solve_task()

man = Pupil('Mike')
man.solve_task()