#  PythonCourse/Lectures/PyLec_5.pdf Task №3

from tempfile import mktemp
from os import path 
from os import remove

class WrapStrToFile:
    
    def __init__(self):
        self.filepath = mktemp(".txt", "test")

    @property
    def content(self):
        try:
            file = open(self.filepath, "r")
            text = file.read()
            file.close()
            return "Output: {}".format(text)
        except IOError as e:
            return "Output: File does't exist"
    

    @content.setter
    def content(self, value):
        file = open(self.filepath, "w")
        file.write(value)
        file.close()
        return file

    @content.deleter
    def content(self):
        remove(self.filepath)


wstf = WrapStrToFile()
print(wstf.content)
wstf.content = 'test str'
print(wstf.content)
wstf.content = 'text 2'
print(wstf.content)
del wstf.content
