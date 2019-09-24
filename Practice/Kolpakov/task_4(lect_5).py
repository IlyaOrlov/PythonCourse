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


#Num 3
import tempfile
import os

class WrapStrToFile:
    def __init__(self):
        self.filepath = tempfile.mktemp()

# здесь инициализируется атрибут filepath,
# он содержит путь до файла-хранилища
    @property
    def content(self):
        try:
            fo = open(self.filepath, 'r')
        except FileNotFoundError:
            return "File doesn't exist"
        except Exception as exc:
            return "Some unexpected error: {}".format(exc)
        else:
            return fo.read()

# попытка чтения из файла, в случае успеха возвращаем содержимое
# в случае неудачи возвращаем 'File doesn't exist'
    @content.setter
    def content(self, value):
        fo = open(self.filepath, 'w')
        fo.write(value)
        fo.close()

# попытка записи в файл указанного содержимого
    @content.deleter
    def content(self):
        os.remove(self.filepath)


wstf = WrapStrToFile()
print(wstf.content)  # Output: File doesn't exist
wstf.content = 'test str'
print(wstf.content)  # Output: test_str
wstf.content = 'text 2'
print(wstf.content)  # Output: text 2
del wstf.content
# после этого файла не существует
