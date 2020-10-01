import time


def test_func(a, b):
    return a + b


class MyManager:
    def __enter__(self):
        self.start_time = time.clock()
        print("Starting code inside manager")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.clock()
        self.result = self.end_time - self.start_time
        print(f"Ending code inside manager. Runtime - {self.result}")


with MyManager():
    print(test_func(4759465804756475649736076740367485746985, 50000000000))
