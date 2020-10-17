import time


class Timer:
    _begin = 0

    def __enter__(self):
        Timer._begin = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"it took {time.time() - Timer._begin:.3f} sec")


if __name__ == "__main__":
    with Timer():
        some_list = list(range(1000000))
