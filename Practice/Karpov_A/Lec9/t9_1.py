import time
import threading


def find_primes(start, end):
    primes = []
    start_time = time.time()
    for i in range(start, end + 1):
        if i > 1:
            for n in range(2, i):
                if (i % n) == 0:
                    break
            else:
                primes.append(i)
    print(f"Диапазон от {start} до {end}, время обработки {time.time() - start_time} сек.")
    return primes

begin = [3, 10001, 20001]
finish = [10000, 20000, 30000]

start_seq = time.time()
for i in range(3):
    find_primes(begin[i], finish[i])
print(f"Общее время: {time.time() - start_seq} сек.")

start_thr = time.time()
threads = []
for i in range(3):
    thread = threading.Thread(target=find_primes, args=(begin[i], finish[i]))
    threads.append(thread)
    thread.start()
for thr in threads:
    thr.join()
print(f"Многопоцессорность: {time.time() - start_thr}")