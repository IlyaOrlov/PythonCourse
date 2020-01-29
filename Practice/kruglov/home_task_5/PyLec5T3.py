#  PythonCourse/Lectures/PyLec_5.pdf Task №3

from tempfile import mktemp
from os import remove


class WrapStrToFile:

    def __init__(self):
        self.filepath = mktemp(".txt", "test")

    @property
    def content(self):
        try:
            with open(self.filepath, "r") as file:
                text = file.read()
                return "Output: {}".format(text)
        except IOError:
            return "Output: File does't exist"

    @content.setter
    def content(self, value):
        with open(self.filepath, "w") as file:
            file.write(value)
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
