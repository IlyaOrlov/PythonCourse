#1
import threading
import multiprocessing
import time

def isPrime(a):
    return all(a % i for i in range(2, a))

def find_primes(end,start=3):
    return [x for x in range(start, end) if isPrime(x)]

def without_all():
    start = time.perf_counter()
    find_primes(10000)
    find_primes(20000, 10001)
    find_primes(30000, 20001)
    print('Время вычислений без многопоточности: {}'.format(int(time.perf_counter() - start)))

def with_threading():
    thrs = [threading.Thread(target=find_primes, args=(10000, 3)),
            threading.Thread(target=find_primes, args=(20000, 10001)),
            threading.Thread(target=find_primes, args=(30000,20001))]

    start = time.perf_counter()
    for thr in thrs:
        thr.start()
    for thr in thrs:
        thr.join()
    print('Время вычислений с threading: {}'.format(int(time.perf_counter() - start)))

def with_multiprocessing():
    mps = [multiprocessing.Process(target=find_primes, args=(10000, 3)),
           multiprocessing.Process(target=find_primes, args=(20000, 10001)),
           multiprocessing.Process(target=find_primes, args=(30000, 20001))]
    start = time.perf_counter()
    for mp in mps:
        mp.start()
    for mp in mps:
        mp.join()
    print('Время вычислений с multiprocessing: {}'.format(int(time.perf_counter() - start)))


if __name__ == '__main__':

    without_all()
    with_threading()
    with_multiprocessing() #самый быстрый способ



