import time


class Timer:
    def __enter__(self):
        self._time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Total execution time of your code is {:0.6f} second.'.format((self._time - time.time()) * -1))


if __name__ == "__main__":
    with Timer():
        time.sleep(1)
