from random import randint
from time import sleep
from L5T1 import Man


class Pupil(Man):
    def solve_task(self):
        print("thinking...")
        time = randint(3, 6)
        sleep(time)
        print("I'm ready")


man = Man("karlson")
man.solve_task()
pupil = Pupil("malysh")
pupil.solve_task()
