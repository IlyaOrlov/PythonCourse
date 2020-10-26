# Напишите свой менеджер контекста, замеряющий и показывающий время исполнения кода внутри него.

import time

class TestManager:
    def __enter__(self):
        self.currTime = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        timeInterval = time.time() - self.currTime
        print('Running time {}'.format(timeInterval))

with TestManager():
    n = 99999
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i