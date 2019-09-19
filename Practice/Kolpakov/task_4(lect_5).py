from time import sleep
from random import randint
#Num 1
class Man:
    def __init__(self, name, first_name):
        self.name = name
        self.first_name = first_name

    def solve_task(self):
        return "I'm not ready yet"

a = Man('Armen', 'Grigorjan')
print(a.solve_task())


#Num 2
class Pupil(Man):
    def __init__(self, name, first_name):
        super().__init__(name, first_name)

    def solve_task(self):
        print('Please wait....')
        sleep(randint(3, 6))
        return "I'm not ready yet"

b = Pupil('Mark', 'Tven')
print(b.solve_task())