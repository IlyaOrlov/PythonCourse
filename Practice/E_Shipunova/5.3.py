import os
#import tempfile - I can not use the library, because my interpreter trows Error already at import
import datetime                            # only for unique file_path


class WrapStrToFile:
    id = 0                                 # only for unique file_path

    def __init__(self):
        WrapStrToFile.id += 1              # only for unique file_path
        self.file_path = str(WrapStrToFile.id)+"_"+str(datetime.date.today())+".txt"  # have to be 'tempfile.mktemp()'

    @property                              # get file_content
    def content(self):
        try:
            f = open(self.file_path, 'r')
        except FileNotFoundError:
            return "File doesn't exist"
        else:
            file_content = f.read()        # if the file is open
            f.close()                      # I don't write 'finally', because
                                           # if the file is closed, we can not close it
        return file_content

    @content.setter                        # set file_content
    def content(self, value):
        f = open(self.file_path, 'w')
        f.write(value)
        f.close()

    @content.deleter
    def content(self):
        os.remove(self.file_path)


if __name__ == "__main__":
    wstf = WrapStrToFile()
    print(f"File_path is '{wstf.file_path}'")
    print(wstf.content)
    wstf.content = "test str"
    print(wstf.content)
    wstf.content = "test2"
    print(wstf.content)
    del wstf.content
