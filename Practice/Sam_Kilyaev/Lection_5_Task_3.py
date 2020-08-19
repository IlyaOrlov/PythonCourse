import tempfile
import os


class WrapStrToFile:
    def __init__(self):
        self.filepath = tempfile.mktemp()

    @property
    def content(self):
        try:
            with open(self.filepath, "r") as self.fp:
                return self.fp.read()

        except OSError:
            return "File not found"

    @content.setter
    def content(self, value):
        self.value = value
        with open(self.filepath, "w") as self.fp:
            self.fp.write(self.value)

    @content.deleter
    def content(self):
        os.remove(self.filepath)


A = WrapStrToFile()
print(A.content)
A.content = 'Hello World'
print(A.content)
del A.content
print(A.content)
