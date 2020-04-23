import time
import itertools

class t:
    def __init__(self):
        self.time = 0
    def __enter__(self):
        self.time = time.time()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Время равно:{}".format(time.time() - self.time))
with t():
    lst = []
    for i in range(1000000):
        lst.append(i**2)


print(list(itertools.combinations("password", 4)))
print(list(itertools.filterfalse(lambda x: len(x) < 5, ["hello", "i", "write", "cool", "code"])))
print(list(itertools.chain([1, 2, 3], [4, 5], [6, 7])))
