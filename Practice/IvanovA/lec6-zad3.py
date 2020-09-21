import time

class TimeCounter:

    def __enter__(self):
        self.start_time = time.perf_counter()
        print('Start')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.perf_counter() - self.start_time
        print('operating time {}'.format(self.end_time))

with TimeCounter():
    lst = []
    for i in range(1, 10000000):
        lst.append(i ** 2)
