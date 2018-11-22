# -*- coding: utf-8 -*-
#for Python 2.7
#lecture 4 task 3

from tempfile import mktemp
from os import remove

class WrapStrToFile(object):

    def __init__(self):
    #здесь инициализируется атрибут filepath,
    #содержащий путь к хранилищу
        self.filepath =  mktemp(".txt")

    @property
    def content(self):
        #попытка чтения из файла, в случае успеха возвращает его содержимое
        #в случае неудачи возвращает "File doesn't exist"
        try:
            with open(self.filepath, "r") as fread:
                return fread.read()
        except IOError:
            return "File doesn't exist"
    
    @content.setter
        #попытка записи в файл указанного содержимого
    def content(self, value):
        with open(self.filepath, "w") as fwrite:
            fwrite.write(value)

    @content.deleter
        #удаление файла
    def content(self):
        remove(self.filepath)
        
        
if __name__ == '__main__':
    wstf = WrapStrToFile()
    print wstf.filepath
    print wstf.content
    wstf.content = "Some test string"
    print wstf.content
    wstf.content = "Some other string"
    print wstf.content
    del wstf.content
    print wstf.content
    



