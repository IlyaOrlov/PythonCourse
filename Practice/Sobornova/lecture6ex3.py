import time


class TimeCode:
    def __enter__(self):
        self.start = time.time()
        print("Время начала работы кода: " + str(self.start) + '.')

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print("Время исполнения кода составляет: " + str(end - self.start) + ' секунд.')


with TimeCode():
    print(5+5)
