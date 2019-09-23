"""
1. We generate an instance of class WrapStrToFile,
create a name of a temporary file as his attribute 'filepath'.
2. With property content we try to read the content of this file
(may be it exists) and retirn this content.
If it does not exist we return warning.
3. Either file exists, or it does not - we set the content of the file
(and thus the file itself).
4.  Finally we make a property to delete this file.
/gentleman must clean up after himself/
Note: I think that 'except' can be omitted in this peculiar case.
Only 'try' and 'finally'.
=== ===
v.2: try/except block included in @content.setter
"""

from os import remove
from tempfile import mktemp

class WrapStrToFile:
    def __init__(self):
        self.filepath = mktemp()  # generate the name of file,
        # but do not create the file

    @property
    def content(self):
        substance = 'Hey, this file does not exist.'
        # I think it is easier way to produce warning - without 'except'.
        # We should define it in 1st line after def
        # and than do 'try' and 'finally'.
        # But for tutorial reason I include except for particular error.
        try:
            fo = open(self.filepath, 'r')  # May be this file exists.
            substance = fo.read()
            fo.close()
        except FileNotFoundError as ex:  # If the file does not exist.
            #
            substance = 'File is not found'
        finally:
            return substance

    @content.setter
    def content(self, value):  # We create file and its content.
        try:
            fo = open(self.filepath, 'w')
            fo.write(value)
            fo.close()
        except :
            print('Something goes wrong with writing...')



    @content.deleter
    def content(self):  # We delete file.
        os.remove(self.filepath)


wstf = WrapStrToFile()
print('Filepath is: ' + wstf.filepath)
print(wstf.content)
print('')

wstf.content = 'Try to write'
print(wstf.content)
print('')

wstf.content = 'Itsy bitsy spider'
print(wstf.content)