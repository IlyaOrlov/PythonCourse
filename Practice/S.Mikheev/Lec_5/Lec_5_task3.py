import os
import tempfile


class WrapStrToFile:
    def __init__(self):
        self.filepatch = tempfile.mktemp()

    @property
    def content(self):
        try:
            f = open(self.filepatch, 'r')
        except  FileNotFoundError:  # Ошибка если файл не найден
            return "File doesn't exist."
        except Exception as exc:
            return "Some unexpected error: {}".format(type(exc).__name__)
        else:
            return f.read()

    @content.setter
    def content(self, value):
        try:
            f = open(self.filepatch, 'w')
        except PermissionError:  # Ошибка недостаточно прав для записи
            return "Editing is not available."
        except Exception as exc:
            return "Some unexpected error: {}".format(type(exc).__name__)
        else:
            f.write(value)
        finally:
            f.close()

    @content.deleter
    def content(self):
        os.remove(self.filepatch)


wstf = WrapStrToFile()
print(wstf.content)
wstf.content = 'test str'
print(wstf.content)
wstf.content = 'test str new'
print(wstf.content)
del wstf.content