import math


class Iterator:
    def __init__(self, high: int):
        self.high = high
        self.current = 1
        self.counter = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > self.high:
            raise StopIteration
        else:
            self.counter += 1
            while True:
                self.current += 1
                if self.current == 2:
                    break
                lim = math.ceil(math.sqrt(self.current))
                result = True
                for i in range(2, lim + 1):
                    if self.current % i == 0:
                        result = False
                        break
                if result:
                    break
            return self.current
