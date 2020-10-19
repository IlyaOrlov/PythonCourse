import os
import tempfile


class WrapStrToFile:
    def __init__(self):
        self.stream, self.filepath = tempfile.mkstemp(suffix='.txt', prefix='temp', dir=None, text=True)
        os.close(self.stream)

    @property
    def content(self):
        try:
            with open(self.filepath, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "File doesn't exist"

    @content.setter
    def content(self, string):
        with open(self.filepath, 'w') as file:
            file.write(string)

    @content.deleter
    def content(self):
        os.remove(self.filepath)


wstf = WrapStrToFile()
print(f"content={wstf.content}")
wstf.content = 'test text1'
print(f"content={wstf.content}")
wstf.content = 'test text2'
print(f"content={wstf.content}")
del wstf.content
print(f"content={wstf.content}")
