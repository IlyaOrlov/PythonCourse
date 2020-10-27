#ЛЕКЦИЯ ПЯТЬ
#task one
class Man:
    def __init__(self,name):
        self.name=name

    def solve_task(self):
        print ("I'm not ready yet")
man = Man("Vasya")
man.solve_task()

#task two
import time
import random

class Pupil(Man):
    def __init__(self,name):
        super().__init__(name)

    def solve_task(self):
        a = random.randint(3,6)
        time.sleep(a)
        print("I'm not ready yet")

p = Pupil('Vasya')
p.solve_task()

#task three
import tempfile
import os
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


wstf = WrapStrToFile()
print(wstf.content) # Output: File doesn't exist
wstf.content = 'test str'
print(wstf.content) # Output: test_str
wstf.content = 'text 2'
print(wstf.content) # Output: text 2
del wstf.content
