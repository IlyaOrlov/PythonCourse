import os
import tempfile


class WrapStrToFile:
    def __init__(self):
        self.filepath = tempfile.mktemp()
        self._content = None

    @property
    def content(self):
        try:
            with open(self.filepath, 'r') as file:
                self._content = file.read()
        except IOError:
            print('File doesn\'t exist!')
        else:
            return self._content

    @content.setter
    def content(self, value):
        self._content = value
        with open(self.filepath, 'w') as file:
            file.write(value)

    @content.deleter
    def content(self):
        os.remove(self.filepath)


wstf = WrapStrToFile()
print(wstf.content)
wstf.content = 'test str'
print(wstf.content)
wstf.content = 'test 2'
print(wstf.content)
del wstf.content