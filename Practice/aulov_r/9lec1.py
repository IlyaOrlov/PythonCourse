import math
import threading
import multiprocessing
import time

def find_primes(start, end):
    a = []
    for b in range(start, end + 1):
        if all(b % i != 0 for i in range(2, int(math.sqrt(b)) + 1)):
            a.append(b)
    return a

if __name__ == '__main__':
    start_t = time.time()
    find_primes(3, 100000)
    find_primes(100001, 200000)
    find_primes(200001, 300000)
    print('Время выполнения: ', time.time() - start_t)

    start_t = time.time()
    threads = [threading.Thread(target=find_primes, args=(3, 100000)),
               threading.Thread(target=find_primes, args=(100001, 200000)),
               threading.Thread(target=find_primes, args=(200001, 300000))]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print('Многопоточность время выполнения: ', time.time() - start_t)

    t = time.time()
    processes = [multiprocessing.Process(target=find_primes, args=(3, 100000)),
                 multiprocessing.Process(target=find_primes, args=(100001, 200000)),
                 multiprocessing.Process(target=find_primes, args=(200001, 300000))]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    print('Многопроцессорная обработка время выполнения: ', time.time() - start_t)