import time

class Time:
    def __init__(self):
        self.start_time = 0

    def __enter__(self):
        self.start_time = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.perf_counter() - self.start_time
        print('Сколько времени прошло {}'.format(self.end_time))


with Time():
    lst = []
    for i in range(1, 10000000):
        lst.append(i ** 2)
