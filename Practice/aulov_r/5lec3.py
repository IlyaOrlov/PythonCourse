import tempfile

class WrapStrToFIle:
    def __init__(self):
        self._filepath = tempfile.mkstemp()

    @property
    def content(self):
        try:
            a = open(self._filepath[1])
        except FileNotFoundError:
            print('not file')
        else:
            a.read()
            a.close()

    @content.setter
    def content(self, value):
        a = open(self._filepath[1], 'w')
        a.write(value)

    @content.deleter
    def content(self):
        self._filepath = 'delete file'

b = WrapStrToFIle()
b.content
