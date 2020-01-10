from tempfile import mktemp
from os import path

class WrapStrToFile:
    
    def __init__(self):
        self.filepath = mktemp(".txt", "test")

    @property
    def content(self):
        # if path.exists(self.filepath):
        #     return open(self.filepath, "r")
        # else:
        #     return "File does't exist"
        try:
            file = open(self.filepath)
        except IOError as e:
            return "File does't exist"
    

    @content.setter
    def content(self, value):
        file = open(self.filepath, "w")
        return file

    @content.deleter
    def content(self):
        pass

wstf = WrapStrToFile()
print(wstf.content)
wstf.content = 'test str'
print(wstf.content)
wstf.content = 'text 2'
print(wstf.content)
del wstf.content