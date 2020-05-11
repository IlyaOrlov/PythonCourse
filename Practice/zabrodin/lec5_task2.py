import time
import random


class Pupil:
    def __init__(self, n, s):
        self.name = n
        self.surname = s
        self.full_name = n + ' ' + s

    def solve_task(self):
        n = random.randint(3, 6)
        time.sleep(n)
        print("I'm not ready yet, {}!".format(self.full_name))


p = Pupil('Igor', 'Zabrodin')
p.solve_task()
