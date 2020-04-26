import tempfile as temp
import os

class WrapStrToFile:

    def __init__(self):
        self.filepath = temp.mktemp()

    @property
    def content(self):
        try:
            with (open(self.filepath)) as f1:
                return f1.read()
        except FileNotFoundError:
            print("файл не существует")
            return None



    @content.setter
    def content(self, value):
        with (open(self.filepath, 'w')) as f1:
            f1.write(value)


    @content.deleter
    def content(self):
        os.remove(self.filepath)


wstf = WrapStrToFile()
print(wstf.content)
wstf.content = 'test str'
print(wstf.content)
wstf.content = 'text 2'
print(wstf.content)
del wstf.content