import time


class TimeCodeExecution:
    def __init__(self):
        self.begin = time.time()

    def __enter__(self):
        print('Время начала исполнения кода {} секунд'.format(str(self.begin)))

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print('Время исполнения кода {} секунд'.format(str(self.end - self.begin)))


# проверка работы
with TimeCodeExecution():
    for i in range(2000):
        print(i*5)