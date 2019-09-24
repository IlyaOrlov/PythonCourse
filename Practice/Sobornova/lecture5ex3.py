import os
import tempfile


class WrapStrToFile:
    def __init__(self):
        self.file_path = tempfile.mktemp('text_task_3.txt')

    @property
    def content(self):
        try:
            with open(self.file_path, 'r') as file_object:
                file = file_object.read()
        except FileNotFoundError:
            error = "File doesn't exist."
            return error
        else:
            return file

    @content.setter
    def content(self, value):
        with open(self.file_path, 'w') as file_object:
            file_object.write(value)

    @content.deleter
    def content(self):
        os.remove(self.file_path)


wstf = WrapStrToFile()
print(wstf.content)
wstf.content = 'test str'
print(wstf.content)
wstf.content = 'test 2'
print(wstf.content)
del wstf.content
