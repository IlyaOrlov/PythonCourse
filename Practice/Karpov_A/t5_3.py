from tempfile import mktemp
from os import path
from os import remove

class WrapStrToFile:

    def __init__(self):
        self.filepath = mktemp(".txt", "exem")

    @property
    def content(self):
        try:
            with open(self.filepath, "r") as file:
                exem = file.read()
                return "Output: {}".format(exem)
        except IOError as file:
            return "Output: File does't exist"


    @content.setter
    def content(self, value):
        with open(self.filepath, "w") as file:
            file.write(value)
            return file

    @content.deleter
    def content(self):
        remove(self.filepath)


wrap = WrapStrToFile()
print(wrap.content)
wrap.content = 'exem one'
print(wrap.content)
wrap.content = 'exem two'
print(wrap.content)
del wrap.content