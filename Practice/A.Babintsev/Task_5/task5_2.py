"""
Написать класс Pupil, у которого переопределен метод solve_task. На
этот раз он будет думать от 3 до 6 секунд (c помощью метода sleep
библиотеки time и randint библиотеки random).
"""
import time
import random


class Man:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login = (first_name[0] + last_name).lower()
    def solve_task():
        print("I'm not ready yet.")

class Pupil(Man):
    def solve_task():
        x = random.randint(3, 6)
        time.sleep(x)
        print("I'm not ready yet to. But I will ready in {} seconds.".format(x))

Man.solve_task()
Pupil.solve_task()
    
