import tempfile
import os


class WrapStrToFIle:
    def __init__(self):
        self._fd, self._filepath = tempfile.mkstemp()

    @property
    def content(self):
        try:
            f = open(self._filepath)
        except FileNotFoundError:
            print('Файл еще не существует')
        else:
            text = f.read()
            f.close()
        return text


    @content.setter
    def content(self, value):
        f = open(self._filepath, 'w')
        f.write(value)
        f.close()


    @content.deleter
    def content(self):
        os.close(self._fd)
        os.remove(self._filepath)


t = WrapStrToFIle()
t.content = 'ABCD'
print(t.content)
print(t._filepath)
del t.content
m = WrapStrToFIle()
m.content = 'Test2'
print(m.content)
print(m._filepath)
