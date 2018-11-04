# 04.11 - [ИО]:  Проверено (есть замечания).
import os


class WrapStrToFile:
    # 04.11 - [ИО]:  Какого предназначение данного поля?
    filepath = None

    def __init__(self):
        # 04.11 - [ИО]:  класс должен инициализовать атрибут filepath,
        # путем присваивания результата функции mktemp библиотеки tempfile
        self.filepath = 'dataBase.txt'

    @property
    def content(self):
        try:
            file = open(self.filepath)
            result = ''
            for i in file:
                result += i
            file.close()
            return result
        # 04.11 - [ИО]:  Желательно отлавливать только определенный тип исключений.
        except Exception:
            return 'File does not exist'

    @content.setter
    def content(self, value):
        try:
            file = open(self.filepath, 'w')
            file.write(value)
        # 04.11 - [ИО]:  Файл должен закрываться после записи.
        except Exception as e:
            print(e)

    @content.deleter
    def content(self):
        os.remove(self.filepath)


wstf = WrapStrToFile()
print(wstf.content)
wstf.content = 'test str'
print(wstf.content)
wstf.content = 'text 2'
print(wstf.content)
del wstf.content

