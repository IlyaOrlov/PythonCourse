import random  #импорт библиотек
import time  #импорт библиотек
class Man:  #объявление класса
    def __init__(self, name):  #конструктор класса
        self.name = name  #объявление переменной класса содержащей имя
    def get_class_name(self):
        return self.__class__.__name__
    def SolveTask(self):  #функция класса
        print("{} not ready yet".format("Man")) #как получить имя класса? Конструкция __class__.__name__ возвращает str

class Pypil(Man):
    def SolveTask(self):
        t = random.randint(3, 6)
        time.sleep(t)
        print("{} not ready yet".format(name))

name = input("input Pypil name")
Man.SolveTask(name)
Pypil.SolveTask(name)
