import os
from tempfile import mktemp


class WrapStrToFile:
    def __init__(self):
        self._filepath = mktemp(suffix='.txt', dir='.')

    @property
    def content(self):
        try:
            f = open(self._filepath, 'r')
            text = f.read()
            f.close()
            return text
        except (IOError, EOFError):
            print("File doesn't exist yet")
            return None

    @content.setter
    def content(self,value):
        try:
            f = open(self._filepath, 'w')
            f.write(value)
            f.close()
        except Exception as exp:
            print ("Unexpected error: {}".format(exp))

    @content.deleter
    def content(self):
        try:
            os.remove(self._filepath)
        except Exception as exp:
            print("Unexpected error: {}".format(exp))

wstf = WrapStrToFile()
print(wstf.content)

wstf.content = "test str"
print(wstf.content)

wstf.content = "text 2"
print(wstf.content)

del wstf.content
print(wstf.content)
