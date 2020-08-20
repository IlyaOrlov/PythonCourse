import random
import time
from task_5_1 import Man


class Pupil(Man):
    def __init__(self, first_name):
        super().__init__(first_name)

    def solve_task(self):
        print('Mmmm....!!')
        time.sleep(random.randint(3, 6))
        print("'I`m not ready either'")

man2 = Pupil("Halk")
print(f"{man2.first_name}:", end = " ")
man2.solve_task()
