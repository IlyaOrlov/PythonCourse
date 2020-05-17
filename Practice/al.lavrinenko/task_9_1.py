import math
import threading
import multiprocessing
import time


def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            primes.append(num)
    return primes


if __name__ == '__main__':
    t = time.time()
    find_primes(3, 100000)
    find_primes(100001, 200000)
    find_primes(200001, 300000)
    print('Execution time: ', time.time() - t)

    t = time.time()
    threads = [threading.Thread(target=find_primes, args=(3, 100000)),
               threading.Thread(target=find_primes, args=(100001, 200000)),
               threading.Thread(target=find_primes, args=(200001, 300000))]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print('Multithreading execution time: ', time.time() - t)

    t = time.time()
    processes = [multiprocessing.Process(target=find_primes, args=(3, 100000)),
                 multiprocessing.Process(target=find_primes, args=(100001, 200000)),
                 multiprocessing.Process(target=find_primes, args=(200001, 300000))]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    print('Multiprocessing execution time: ', time.time() - t)
