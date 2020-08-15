import tempfile
import os


class WrapStrToFile:
    def __init__(self):
        self._filepath = tempfile.mktemp()

    @property
    def content(self):
        try:
            f = open(self._filepath, 'r')
            self._content = f.read()
            f.close()
            return self._content
        except (IOError, EOFError):
            return "file doesn't exist"

    @content.setter
    def content(self, value):
        try:
            f = open(self._filepath, 'w')
            self._content = value
            f.write(self._content)
            f.close()
        except (IOError, EOFError):
            print("file doesn't exist")

    @content.deleter
    def content(self):
        try:
            os.remove(self._filepath)
        except Exception as e:
            print("unexpected error: {}".format(e))


wstf = WrapStrToFile()
print(wstf.content)
wstf.content = "test str"
print(wstf.content)
wstf.content = "text 2"
print(wstf.content)
del wstf.content
print(wstf.content)
