import time


class TestManager:
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('{:.0f} ms'.format((time.time() - self.start_time)*1000))


with TestManager():
    for i in range(10 ** 7):
        pass
