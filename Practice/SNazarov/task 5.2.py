import random
import time


class Man:

    def __init__(self, first_name):
        self.first_name = first_name

    def solve_task(self):
        print("'I`m not ready yet'")

class Pupil(Man):
    def __init__(self, first_name):
        super(Pupil, self).__init__(first_name)

    def solve_task(self):
        print('Mmmm....!!')
        time.sleep(random.randint(3, 6))
        print("'I`m not ready either'")

man = Man("Deadpool")
print(f"{man.first_name}:", end = " ")
man.solve_task()
man2 = Pupil("Halk")
print(f"{man2.first_name}:", end = " ")
man2.solve_task()
