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
    start_threads = time.time()
    th1 = threading.Thread(name='thread_1', target=find_primes(10000))
    th1.start()
    th1.join()
    th2 = threading.Thread(name='thread_2', target=find_primes(20000, 10001))
    th2.start()
    th2.join()
    th3 = threading.Thread(name='thread_3', target=find_primes(30000, 20001))
    th3.start()
    th3.join()
    print("Lead time = {:.2f} sec.".format(time.time() - start_threads))

    start_processes = time.time()
    pr1 = mp.Process(target=find_primes(10000))
    pr1.start()
    pr1.join()
    pr2 = mp.Process(target=find_primes(20000, 10001))
    pr2.start()
    pr2.join()
    pr3 = mp.Process(target=find_primes(30000, 20001))
    pr3.start()
    pr3.join()
    print("Lead time = {:.2f} sec.".format(time.time() - start_processes))
