"""
Написать класс WrapStrToFIle, который будет иметь одно
вычисляемое свойство (property) под названием content. В
конструкторе класс должен инициализовать атрибут filepath, путем
присваивания результата функции mktemp библиотеки tempfile. При
попытке чтения свойства content должен внутри кода свойства
открываться файл, используя атрибут filepath (с помощью функции
open, из этого файла читается все содержимое и возвращается из
свойства. Если файл не существует, то возникает ошибка, поэтому
должна быть обертка вокруг открытия файла на чтение
(try...except), с помощью которого будет возвращаться 'Файл еще не
существует'. При присваивании значения свойству content файл по
указанному пути должен открываться на запись и записываться
содержимое. Не забудьте закрывать файл после чтения или записи.
При удалении атрибута content, должен удаляться и файл.
"""
import os
import tempfile


class WrapStrToFile:
    def __init__(self):
    # здесь инициализируется атрибут filepath,
    # он содержит путь до файла-хранилища
        self.filepath = tempfile.mktemp(suffix='.txt')

    @property
    def content(self):
    # попытка чтения из файла, в случае успеха возвращаем содержимое
    # в случае неудачи возвращаем 'File doesn't exist'
        try:
            test_f = open(self.filepath, 'r')
        except FileNotFoundError:
            return "File doesn't exist"
        else:
            return test_f.read()
    
    @content.setter
    def content(self, value):
    # попытка записи в файл указанного содержимого
        test_f = open(self.filepath, 'w')
        test_f.write(value)
        test_f.close()
    
    @content.deleter
    def content(self):
    # удаляем файл: os.remove(имя_файла)
        os.remove(self.filepath)


wstf = WrapStrToFile()
print(wstf.content) # Output: File doesn't exist
wstf.content = 'test string 1'
print(wstf.content) # Output: test string 1
wstf.content = 'test string 2'
print(wstf.content) # Output: test string 2
del wstf.content # после этого файла не существует 
