import os

class WrapStrToFile:
    def __init__(self, filepath):
        self.filepath = filepath

    # здесь инициализируется атрибут filepath,
    # он содержит путь до файла-хранилища

    @property
    def content(self):
        if os.path.exists(self.filepath) == True:
            with open(self.filepath, "r") as fr:
                fileText = fr.read()
            return fileText

        else:
            return "File doesn't exist"

    # попытка чтения из файла, в случае успеха возвращаем содержимое
    # в случае неудачи возвращаем 'File doesn't exist'

    @content.setter
    def content(self, value):
        with open(self.filepath, "w") as fw:
            fw.write(value)

    # попытка записи в файл указанного содержимого

    @content.deleter
    def content(self):
        os.remove(self.filepath)

    # удаляем файл: os.remove(имя_файла)Практика*


wstf = WrapStrToFile("2")
print(wstf.content)  # Output: File doesn't exist
wstf.content = 'test str'
print(wstf.content)  # Output: test_str
wstf.content = 'text 2'
print(wstf.content)  # Output: text 2
del wstf.content  # после этого файла не существует
