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
                return file.read()

        except IOError as file:
            return "Output: File does't exist"

    @content.setter
    def content(self, value):
        self.value = value
        with open(self.filepath, "w") as file:
            file.write(self.value)

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
