import os
from tempfile import mktemp


class WrapStrToFIle:
    def __init__(self):
        self.filepath=mktemp()
        self._content=None

    @property
    def content(self):
        try:
            with open(self.filepath + "/" + "file.xml", encoding="utf-8") as f:
                self._content = f.read()
        except FileNotFoundError:
            print("Файл еще не существует")
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
        try:
            with open(self.filepath + "/" + "file.xml", 'w', encoding="utf-8") as f:
                f.write(value)
        except FileNotFoundError:
            print("Файл не записан, т.к. указананный файл не существует")
        except Exception as exc:
            print ("Some unexpected error:".format(exc))

    @content.deleter
    def content(self):
        del self._content
        try:
            os.remove(self.filepath + "/" + "file.xml")
        except FileNotFoundError:
            print("Вы пытаетете удалить несуществующий файл")



a=WrapStrToFIle()
#b=a.content
a.content="текст"
#del a.content
