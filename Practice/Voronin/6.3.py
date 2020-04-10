from datetime import datetime

class timeManager():
    def __enter__(self):
        self.start = datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(datetime.now() - self.start)

with timeManager():
    lst = []
    for i in range(10**4):
        if i % 4 == 0:
            lst.append(i)