import random
import time


class Man:
    def __init__(self, name='Василек'):
        self.name = name

    def solve_task(self):
        print('{}, I \'m not ready yet'.format(self.name))


class Pupil(Man):
    def __init__(self, name='Петр'):
        super().__init__(name)

    def solve_task(self):
        wait = random.randint(3, 6)
        time.sleep(wait)
        print('{}, I \'m not ready yet'.format(self.name))


# проверка функции
obj = Pupil('Петя')
obj.solve_task()

obj2 = Pupil()
obj2.solve_task()