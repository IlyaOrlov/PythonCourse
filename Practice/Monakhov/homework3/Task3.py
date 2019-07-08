import tempfile
import os


class WrapStrToFIle:
    filepath = None

    def __init__(self):
        self.filepath = tempfile.mktemp()

    @property
    def content(self):
        try:
            fp = open(self.filepath, 'r')
            return fp.read()
        except FileNotFoundError:
            print("File doesn't exist!")

    @content.setter
    def content(self, value):
        fp = open(self.filepath, 'w')
        fp.write(value)
        fp.close()

    @content.deleter
    def content(self):
        os.remove(self.filepath)


wstf = WrapStrToFIle()
print(wstf.content)
wstf.content = 'test str'
print(wstf.content)
wstf.content = 'text 2'
print(wstf.content)
del wstf.content
