import time

class TestManager:
    def __enter__(self):
        self._start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('time: {}'.format(time.time() - self._start))

with TestManager():
    print("start")
    time.sleep(1)
    print("finish")