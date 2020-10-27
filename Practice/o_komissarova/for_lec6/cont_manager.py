import time


class ContManager:
    def __enter__(self):
        self._start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('time: {}'.format(time.time() - self._start))


with ContManager():
    print("smth is doing")
    time.sleep(10)
    print("smth is done")
