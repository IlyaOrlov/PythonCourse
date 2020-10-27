#ЛЕКЦИЯ ДЕВЯТЬ
#task one
import time as t

def find_primes(end,start):
    starting = t.time()
    list = []
    flag = True
    for key in range(start, end):
        for i in range(2, key):
            if key % i == 0:
                flag = False
                break
        if flag == True:
            list.append(key)

    finish = t.time()
    print(f"Время = {(finish - starting)} секунд")
    return list

for i in range(3):
    starting = t.time()
    find_primes(10000, 3)
    find_primes(20000, 10001)
    find_primes(30000, 20001)
    break
print(" ")

#Task two
from multiprocessing import Process

def adding(*listing):
    start = t.time()
    if isinstance(listing[0], float) or isinstance(listing[0], int):
        buffer = 0
    elif isinstance(listing[0], list):
        buffer = list()
    else:
        buffer = ''

    for key in listing:
        buffer += key
    finish = t.time()
    print('Веремени для сложения типа {}, затрачено {} sec.'.format(type(listing[0]), finish - start))
    print(buffer)

if __name__ == '__main__':
    arr = [
        ('zzzz','aaaa','ccccc'),
        (124.3,15.4,77.8,),
        (122,144,58,),([7,8,9,],
         ['bbb','cccc'],[7.5,45.23,85.6],)
    ]
    def process(function, arr):
      list = []
      for k in arr:
       list.append(Process(target=function, args=k))
      for key in list:
            key.start()
            yield key

    list = list(process(adding, arr))
    for j in list:
        j.join()
