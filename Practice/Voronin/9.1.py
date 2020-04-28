import time
import threading
import multiprocessing

def find_primes(end, start=3):
    lst = list(range(start, end+1))
    for i,x in enumerate(lst):
        if x % 2 == 0:
            lst[i] = 0
        if x > 3 and x % 3 == 0:
            lst[i] = 0
        if x > 5 and x % 5 == 0:
            lst[i] = 0
        if x > 7 and x % 7 == 0:
            lst[i] = 0
    lst1 = []
    for i,x in enumerate(lst):
        if x != 0:
            lst1.append(lst[i])

    return lst1

start = time.time()
print(find_primes(10000))
print(find_primes(20000, 10001))
print(find_primes(30000, 20001))
print(time.time()-start)

start = time.time()
th = threading.Thread(target=find_primes, args=(10000,))
th.start()
th.join()
th1 = threading.Thread(target=find_primes, args=(20000, 10001))
th1.start()
th1.join()
th2 = threading.Thread(target=find_primes, args=(30000, 20001))
th2.start()
th2.join()
print(time.time()-start)

if __name__ == '__main__':
    start = time.time()
    p = multiprocessing.Process(target=find_primes, args=(10000,))
    p.start()
    p.join()
    p1 = multiprocessing.Process(target=find_primes, args=(20000, 10001))
    p1.start()
    p1.join()
    p2 = multiprocessing.Process(target=find_primes, args=(30000, 20001))
    p2.start()
    p2.join()
    print(time.time() - start)