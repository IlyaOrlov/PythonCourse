import random
import time


class Man:

    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print("I'm not ready yet.")


class Pupil(Man):

    def __init__(self, name):
        super().__init__(name)

    def solve_task(self):
        t = random.randint(3, 6)
        print("Waiting time: {} seconds.".format(t))
        time.sleep(t)
        print("I'm not ready yet.")


person = Man('Rick')
person.solve_task()

person2 = Pupil('Max')
person2.solve_task()
