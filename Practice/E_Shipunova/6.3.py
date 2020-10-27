import time


class TimeManager:
    def __enter__(self):
        self._t = time.clock()  #  for process time
        print(self._t)
        print("Code start!")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Code execution took {time.clock()-self._t} sec")


if __name__ == "__main__":
    with TimeManager():
        [x for x in range(10000000)]
