import os
import tempfile as tf


class WrapStrToFile:
    def __init__(self):
        self.file_path = tf.mktemp()

    @property
    def content(self):
        try:
            f = open(self.file_path)
        except FileNotFoundError:
            print("File doesn't exist.")
        except Exception as exc:
            print("Some unexpected error: {}.".format(exc))
        else:
            return self.content

    @content.setter
    def content(self, value):
        f = open(self.file_path, 'w')
        f.write(value)
        f.close()

    @content.deleter
    def content(self):
        os.remove(self.file_path)


wstf = WrapStrToFile()
print(wstf.content)
wstf.content = 'test str'
print(wstf.content)
wstf.content = 'text 2'
print(wstf.content)
del wstf.content
