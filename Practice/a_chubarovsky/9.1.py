import threading
import multiprocessing as mp
import time


def find_primes(end, start=3):
    n = end
    lst = []
    for i in range(start, n + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
    print(lst)


if __name__ == "__main__":
    start_func = time.time()
    find_primes(10000)
    find_primes(20000, 10001)
    find_primes(30000, 20001)
    print("Lead time = {:.2f} sec.".format(time.time() - start_func))
    start_threads = time.time()
    threads = [threading.Thread(target=find_primes(10000)), threading.Thread(target=find_primes(20000, 10001)),
               threading.Thread(target=find_primes(30000, 20001))]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("Lead time = {:.2f} sec.".format(time.time() - start_threads))

    start_processes = time.time()
    processes = [mp.Process(target=find_primes(10000)), mp.Process(target=find_primes(20000, 10001)),
                 mp.Process(target=find_primes(30000, 20001))]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    print("Lead time = {:.2f} sec.".format(time.time() - start_processes))
