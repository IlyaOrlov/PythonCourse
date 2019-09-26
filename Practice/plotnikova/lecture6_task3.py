import time


class ContextManager():
    def __init__(self):
        self.start_time = time.time()

    def __enter__(self):
        print('Starting code inside')
        for i in range(10000): # для нагрузки, чтобы на выходе был не 0
            a = i**2

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("--- %s seconds ---" % (time.time() - self.start_time))


with ContextManager():
    pass

