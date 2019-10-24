import time


class TimeManager:
    def __enter__(self):
        self.start = time.time()
        print("Program started :" + str(self.start))

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print("Program were working :" + str(end - self.start) + 'seconds' )


with TimeManager():
    print(1+1)