import os
import tempfile
class WrapStrToFile:
    def __init__(self):
        self.filepath = tempfile.mktemp('.txt')
    @property
    def content(self):
        try:
            fp = open(self.filepath)
            result = ''
            for i in fp:
                result += i
            fp.close()
            return result
        except FileNotFoundError:
            return 'File does not exist'
    @content.setter
    def content(self, value):
        try:
            fp = open(self.filepath, 'w')
            fp.write(value)
            fp.close()
        except Exception as e:
            print(e)
    @content.deleter
    def content(self):
        os.remove(self.filepath)

wstf=WrapStrToFile()
print(wstf.content)
wstf.content='test_str'
print(wstf.content)
wstf.content = 'text 2'
print(wstf.content)
del wstf.content
