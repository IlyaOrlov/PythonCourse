import time


class Runtime:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Finished in %s seconds" % (time.time() - self.start))


with Runtime():
    s = [i for i in range(10000000)]
