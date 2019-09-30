
import time


class MyRuntime:
    def __enter__(self):
        self.timestart = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Runtime {} seconds'.format(time.time() - self.timestart))


with MyRuntime():
    print(1 + 1)