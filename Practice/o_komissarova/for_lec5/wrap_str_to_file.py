import tempfile
import os


class WrapStrToFile:
    def __init__(self):
        self._filepath = tempfile.mktemp()

    @property
    def content(self):
        try:
            f = open(self._filepath, 'r')
            string = f.read()
            f.close()
            return string
        except (IOError, EOFError):
            return "file doesn't exist"

    @content.setter
    def content(self, value):
        try:
            f = open(self._filepath, 'w')
            f.write(value)
            f.close()
        except Exception as e:
            print("unexpected error: {}".format(e))

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
