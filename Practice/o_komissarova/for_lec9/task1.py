import multiprocessing
import threading
import time


def find_primes(start, end):
    lst = []
    for i in range(start, end + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    print(len(lst))
    return lst


start_time = time.time()
find_primes(3, 10000)
find_primes(10001, 20000)
find_primes(20001, 30000)
execution_time = time.time() - start_time
print(execution_time)

start_time = time.time()
threads = [threading.Thread(target=find_primes, args=(3, 10000)),
           threading.Thread(target=find_primes, args=(10001, 20000)),
           threading.Thread(target=find_primes, args=(20001, 30000))]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
execution_time = time.time() - start_time
print(execution_time)

start_time = time.time()
processes = [multiprocessing.Process(target=find_primes, args=(3, 10000)),
             multiprocessing.Process(target=find_primes, args=(10001, 20000)),
             multiprocessing.Process(target=find_primes, args=(20001, 30000))]
for process in processes:
    process.start()
for process in processes:
    process.join()
execution_time = time.time() - start_time
print(execution_time)

# if forget start() there will be AssertionError: can only join a started thread/process

# if forget join() execution time will be count and printed earlier,
# because we don't wait for the end of threads/processes
