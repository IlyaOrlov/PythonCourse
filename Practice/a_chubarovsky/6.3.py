import time


def benchmark(func):
    def wrapper(*args, **kwargs):
        t = time.process_time()
        res = func(*args, **kwargs)
        print("{} spent {}".format(func.__name__, time.process_time() - t))
        return res
    return wrapper


class MyContextManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, "w+")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


@benchmark
def new_func(file_name):
    with MyContextManager(file_name) as f:
        f.write("Hello World!!!")
        data = f.read()
    return data


print(new_func("My_file.txt"))
