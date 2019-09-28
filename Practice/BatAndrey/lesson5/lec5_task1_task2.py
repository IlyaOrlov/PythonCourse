# class Man:      #работает
#     """ Принимает имя в конструкторе и выводит "I'm not ready yet" """
#     def __init__(self, name):
#         self.name = name
#
#     def solve_task(self):
#         print("I'm not ready yet")
#
#
# a = Man('nik')
# a.solve_task()


from time import sleep
from random import randint


class Man:
    """ Принимает имя в конструкторе и выводит "I'm not ready yet" """

    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print("I'm not ready yet")


a = Man('nik')
a.solve_task()


class Pupil(Man):
    def solve_task(self):
        sleep(randint(3, 6))
        print("I sleep")


b = Pupil('nik2')
b.solve_task()

