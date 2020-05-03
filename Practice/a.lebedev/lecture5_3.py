import tempfile as tf
import os
import shutil

class WrapStrToFile:
    def __init__(self): # здесь инициализируется атрибут filepath, # он содержит путь до файла-хранилища
        fd, self.path = tf.mkstemp('.txt', 'first', 'test')
        print('file was created')
        os.close(fd)

    @property
    def content(self): # попытка чтения из файла, в случае успеха возвращаем содержимое
        # в случае неудачи возвращаем 'File doesn't exist'
        try:
            with open(self.path, 'r') as file_open:
                # print('file contented next information {}'.format(file_open.readlines()))
                return file_open.readlines()
        except FileExistsError:
            print('File does not exist')


    @content.setter
    def content(self, value): # попытка записи в файл указанного содержимого
        with open(self.path, 'wt') as file_open:
            file_open.writelines(value)
        shutil.copy(self.path, "C:\\Users\\Home\\PycharmProjects\\mytest\\test\\temp.txt")  #тест файл для отслеживания

    @content.deleter
    def content(self): # удаляем файл: os.remove(имя_файла)
        os.remove(self.path)
        print('file was delete')

wstf = WrapStrToFile()
wstf.content
wstf.content = 'hello world'
wstf.content
wstf.content = 'Wow it work'
wstf.content
del wstf.content

