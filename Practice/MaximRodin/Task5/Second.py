import time
import random

class Man:
    def __init__(self, name, surname):
       self.name = name
       self.surname = surname
       self.login = (name[0] + surname).lower()
    def solve_task(self):
        print("I am ready")

class Pupil(Man):
    def solve_task(self):
        a = random.randint(3,6)
        time.sleep(a)
        print("I'm ready now.But I needed {} seconds to wake up.".format(a))
Worker1 = Man("Max", "Rodin")
print(Worker1.login)
Worker1.solve_task()
Worker2 = Pupil("Egor", "Egorov")
print(Worker2.login)
Worker2.solve_task()


