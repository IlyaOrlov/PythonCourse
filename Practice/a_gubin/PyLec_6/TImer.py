import time


class Timer:
    def __init__(self):
        self._begin = 0

    def __enter__(self):
        self._begin = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"it took {time.time() - self._begin:.3f} sec")
        return False


if __name__ == "__main__":
    with Timer():
        some_list = list(range(1000000))
