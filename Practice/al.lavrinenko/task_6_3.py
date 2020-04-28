import time


class ExecTime:
    def __init__(self):
        self.start_time = 0

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Code execution time: {time.time() - self.start_time} seconds")


with ExecTime():
    lst = []
    for i in range(1, 10000000):
        lst.append(i**2)
