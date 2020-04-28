import tempfile

class WrapStrToFile:
    def __init__(self): # здесь инициализируется атрибут filepath, # он содержит путь до файла-хранилища
        self.file = open("111", 'w')
        self.file.read
        print(self.file)


    @property
    def content(self): # попытка чтения из файла, в случае успеха возвращаем содержимое # в случае неудачи возвращаем 'File doesn't exist'
        # a = self.file()
        # print(a)
        pass


    @content.setter
    def content(self, value): # попытка записи в файл указанного содержимого
        self.file.writelines(value)

    @content.deleter
    def content(self): # удаляем файл: os.remove(имя_файла)
        pass


q = WrapStrToFile()
q.content
print (q)
# print(q.content)