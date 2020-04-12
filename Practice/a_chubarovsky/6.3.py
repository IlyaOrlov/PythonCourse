import time
import sys


class MyContextManager:
    def __init__(self, file_name, func_name):
        self.file_name = file_name
        self.func_name = func_name

    def __enter__(self):
        self.file = open(self.file_name, "w+")
        self.t = time.process_time()
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("{} spent {}".format(self.func_name.__name__, time.process_time() - self.t))
        self.file.close()


def new_func(file_name):
    with MyContextManager(file_name, new_func) as f:
        x = 'Spam!'
        f.write(f"{sys.platform}\n{str(2**100)}\n{str(x * 10)}")
        data = f.read()
    return data


print(new_func("My_file.txt"))
