import time


class MyManager:

    def __enter__(self):

        self.start = time.process_time()
        print(f'Start - {self.start} sec')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Code completed  -  {time.process_time() - self.start} sec')

arr = []


def numbers(num):

    global arr
    for i in range(num):
        if i % 15 == 0:
            arr.append('Fizz')
        elif i % 5 == 0:
            arr.append('Buzz')
        elif i % 3 == 0:
            arr.append('FizzBuzz')
        else:
            arr.append(i)

    return arr


with MyManager():
    numbers(10000000)

