# Задание 1, 2 Лекция 5
import time
import random


class Man():
    def __init__(self, name):
        self.name = name

    def solve_task(self):
        return(self.name + " says: I'm not ready yet!")




class Pupil(Man):
    def solve_task(self):
        a = random.randint(3, 6)
        time.sleep(a)
        return (self.name + " says: I'm not ready yet!")

man1 = Man('Mike')
print(man1.solve_task())

child = Pupil('Joe')
print(child.solve_task())

child2 = Pupil('Wess')
print(child2.solve_task())

man2 = Man('Steff')
print(man2.solve_task())
