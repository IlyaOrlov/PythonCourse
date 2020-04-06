from task_5_1 import Man
import time
import random


class Pupil(Man):
    def solve_task(self):
        time.sleep(random.randint(3, 6))
        super().solve_task()


p1 = Pupil('Julian')
print(p1.name)
p1.solve_task()
