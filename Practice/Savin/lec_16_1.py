import time


class Scheduller:

    def __init__(self, operating_time=None):
        if operating_time is None:
            self.operating_time = time.time()
        else:
            self.operating_time = operating_time
        self.functions = []

    def run(self):
        print('Start')
        time_start = time.time()
        while time.time() - time_start < self.operating_time:
            for func in reversed(self.functions):
                time_now = time.time()
                if time_now - func['creation_time'] > func['period']:
                    result = func['func']
                    if result:
                        print(f'Result: {result}')
                    del self.functions[self.functions.index(func)]
        print('Finish')

    def append(self, func, period):
        d = {'func': func, 'period': period, 'creation_time': time.time()}
        self.functions.append(d)


def sum(a, b):
    return a + b

def min(a, b):
    a - b

def mul(a, b):
    return a * b

def delen(a, b):
    return a / b

s = Scheduller(9)
s.append(sum(5, 5), 5)
s.append(min(5, 5), 7)
s.append(mul(5, 5), 8)
s.append(delen(5, 5), 10)
s.run()
