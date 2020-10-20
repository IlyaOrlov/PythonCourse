#1
import time
import random

class Man(object):
    def __init__(self,name):
        self.name = name

    def solve_task(self):
        print("I'm not ready yet")

#2
class Pupil(Man):
    def solve_task(self):
        time.sleep(random.randint(3, 6))
        print("I'm not ready yet")

#3
import tempfile
import os

class WrapStrToFile(object):
    def __init__(self):
        self.filepath = tempfile.mktemp()
    @property
    def content(self):
        try:
            f = open(self.filepath, "r")
            line = "".join(f.readlines())
            f.close()
            return line
        except FileNotFoundError:
            print("File doesn't exist")
            return ''
    @content.setter
    def content(self, value):
        try:
            f = open(self.filepath, "w")
            f.write(str(value))
            f.close()
        except FileNotFoundError:
            print("File doesn't exist")
    @content.deleter
    def content(self):
        os.remove(self.filepath)

man = Man("Ivan")
man.solve_task()

pupil = Pupil("Vasya")
pupil.solve_task()

wstf = WrapStrToFile()
print(wstf.content)
wstf.content = "test str qwer"
print(wstf.content)
wstf.content = "text 2 asdf"
print(wstf.content)
del wstf.content