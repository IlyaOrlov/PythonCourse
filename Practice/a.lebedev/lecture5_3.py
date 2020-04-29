import tempfile as tf
import os

class WrapStrToFile:
    def __init__(self): # здесь инициализируется атрибут filepath, # он содержит путь до файла-хранилища
        self.path = tf.mkstemp('.txt', 'first', 'test')[1]
        print('v peremennoy self.path = ', self.path)
        # print('v peremennoy self.content ', self.content)

    @property
    def content(self): # попытка чтения из файла, в случае успеха возвращаем содержимое
        # в случае неудачи возвращаем 'File doesn't exist'
        try:
            with open(self.path, 'r') as file_open:
                # self.content =
                print(365)
            # return file_open.read()

        except FileExistsError:
            print('File does not exist')

    @content.setter
    def content(self, value): # попытка записи в файл указанного содержимого
        with open(self.path, 'wt') as file_open:
            file_open.write(value)

    @content.deleter
    def content(self): # удаляем файл: os.remove(имя_файла)
        os.remove(self.path)
        print('dannye udaleny')

wstf = WrapStrToFile()
wstf.content
wstf.content = '1234'
try:
    del wstf.content
except PermissionError:
    print('FILE OPEN IN OTHER APP')
