from tempfile import mktemp

class WrapStrToFile:
    
    def __init__(self):
        self.filepath = mktemp(".txt", "test")

    @property
    def content(self):
        
        return open(self.filepath, "w")

    @content.setter
    def content(self, value):
        pass

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