import random
import time
import os
import tempfile


# Написать класс Man который принимает имя в конструкторе Имеет
# метод solve_task который просто выводит I'm not ready yet

class Man:
    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print('I am not ready yet')


first_man = Man("Master")
first_man.solve_task()
print(first_man.name)


# Написать класс Pupil у которого переопределен метод solve_task На
# этот раз он будет думать от 3 до 6 секунд (c помощью метода sleep
# библиотеки time и randint библиотеки random

class Pupil(Man):
    def __init__(self, name):
        super(Pupil, self).__init__(name)

    def solve_task(self):
        time.sleep(random.randint(3, 6))
        print('Am I ready now?')


second_man = Pupil("Yeshua")
second_man.solve_task()
print(second_man.name)


# Написать класс WrapStrToFIle который будет иметь одно
# вычисляемое свойство property под названием content В
# конструкторе класс должен инициализовать атрибут filepath путем
# присваивания результата функции mktemp библиотеки tempfile При
# попытке чтения свойства content должен внутри кода свойства
# открываться файл, используя атрибут filepath (с помощью функции
# open из этого файла читается все содержимое и возвращается из
# свойства Если файл не существует, то возникает ошибка, поэтому
# должна быть обертка вокруг открытия файла на чтение
# try except с помощью которого будет возвращаться 'Файл еще не
# существует' При присваивании значения свойству content файл по
# указанному пути должен открываться на запись и записываться
# содержимое Не забудьте закрывать файл после чтения или записи
# При удалении атрибута content должен удаляться и файл

class WrapStrToFile:
    def __init__(self):
        self.filepath = tempfile.mktemp()

    @property
    def content(self):
        try:
            file = open(self.filepath, 'r')
            string = file.read()
            file.close()
            return string

        except OSError:
            return "File not found"

    @content.setter
    def content(self, value):
        try:
            file = open(self.filepath, 'w')
            file.write(value)
            file.close()
        except Exception as ex:
            print("Unexpected error: {}".format(ex))

    @content.deleter
    def content(self):
        try:
            os.remove(self.filepath)
        except Exception as ex:
            print("Unexpected error: {}".format(ex))


first = WrapStrToFile()
print(first.content)
first.content = 'Test'
print(first.content)
del first.content
print(first.content)
