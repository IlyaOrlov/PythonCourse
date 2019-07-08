import tempfile
import os


class WrapStrToFile(object):

    def __init__(self):
        self.filepath = tempfile.mktemp()


# здесь инициализируется атрибут filepath,
# он содержит путь до файла-хранилища
    @property
    def content(self):
        try:
            fo = open(self.filepath, "r")
            content = fo.read()
            fo.close()
            return content
        except FileNotFoundError:
            return "Файл еще не существует!"



# попытка чтения из файла, в случае успеха возвращаем содержимое
# в случае неудачи возвращаем 'File doesn't exist'
    @content.setter
    def content(self, value):
        fo = open(self.filepath, "w")
        fo.write('Value: ' + str(value))
        fo.close()


# попытка записи в файл указанного содержимого
    @content.deleter
    def content(self):
        os.remove(self.filepath)


# удаляем файл: os.remove(имя_файла)


wstf = WrapStrToFile()
print(wstf.filepath)
print(wstf.content)
wstf.content = 'test_str'
print(wstf.content)
wstf.content = 'text2'
print(wstf.content)
del wstf.content