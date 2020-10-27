import time

class Wait:
    def __init__(self):
        self.begint = 0

    def __enter__(self):
        self.begint = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Around time: {time.time() - self.begint} seconds")

with Wait():
    arr = []
    for i in range(1, 10000000):
        arr.append(i**2)