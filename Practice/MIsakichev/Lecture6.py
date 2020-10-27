#ЛЕКЦИЯ ШЕСТЬ
#task three
import time
class Calculate_time:
    def __init__(self):
        self.start = 0

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Time of execution is =  {time.time() - self.start}")


with Calculate_time():
    buffer = []
    for k in range(1, 10000000):
        buffer.append(k**2)

#task four
import itertools as it
def list_transform(arr):
   list(it.chain([1, 2, 3], [4, 5], [6, 7]))
   print(list(it.filterfalse(lambda x: len(x) < 5, arr)))
   return list(it.combinations("testing", 4))

a = ['Hello','my','name','is','Vasya']
print(list_transform(a))
