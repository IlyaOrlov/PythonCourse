import tempfile
import os


class WrapStrToFile:
    def __init__(self):
        self.filepath = tempfile.mktemp()

    @property
    def content(self):
        try:
            with open(self.filepath, "r") as f:
                return f.read()

        except FileNotFoundError:
            return "File does not exist!"

    @content.setter
    def content(self, value):
        with open(self.filepath, "w") as f:
            f.write(value)

    @content.deleter
    def content(self):
        os.remove(self.filepath)

wstf = WrapStrToFile()
print(wstf.content)
wstf.content = 'test srt'
print(wstf.content)
wstf.content = 'text 2'
print(wstf.content)
del wstf.content
print(wstf.filepath)

