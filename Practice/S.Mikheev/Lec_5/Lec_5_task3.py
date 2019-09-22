import os


class WrapStrToFile:
    def __init__(self):
        self.filepatch = 'test.txt'

    @property
    def content(self):
        try:
            f = open(self.filepatch, 'r')
        except Exception as exc:  # Можно написать: except FileNotFoundError:
            return "File doesn't exist. Exception name: {}".format(type(exc).__name__)
        else:
            return f.read()

    @content.setter
    def content(self, value):
        f = open(self.filepatch, 'w')
        f.write(value)
        f.close()

    @content.deleter
    def content(self):
        os.remove(self.filepatch)


wstf = WrapStrToFile()
print(wstf.content)
wstf.content = 'test str'
print(wstf.content)
wstf.content = 'test str new'
print(wstf.content)
del wstf.content
