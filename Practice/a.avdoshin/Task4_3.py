import os


class WrapStrToFile:
    filepath = None

    def __init__(self):
        self.filepath = 'dataBase.txt'

    @property
    def content(self):
        try:
            file = open(self.filepath)
            result = ''
            for i in file:
                result += i
            file.close()
            return result
        except Exception:
            return 'File does not exist'

    @content.setter
    def content(self, value):
        try:
            file = open(self.filepath, 'w')
            file.write(value)
        except Exception as e:
            print(e)

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

