# 04.11 - [ИО]:  Проверено (есть замечания).
# 04.11 - [ИО]: Добавьте создание объекта класса Man, чтоб
# протестировать решение для первого задания
from random import randint
from time import sleep


class Man:
    # 04.11 - [ИО]: Зачем нужно это поле?
    name = 'Some Man'

    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print('Hello! I am', self.name, 'I am not ready yet')


class Pupil(Man):
    # 04.11 - [ИО]: Зачем нужно это поле?
    name = 'Some Pupil'
    def __init__(self, name):
        super().__init__(name)

    def solve_task(self):
        t = randint(3, 6)
        print('I am thinking...')
        sleep(t)
        print('Hello! I am', self.name, 'I am not ready yet')


Bob = Pupil('Bob')
Bob.solve_task()
