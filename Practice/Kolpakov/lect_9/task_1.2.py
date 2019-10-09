import time
import threading


def find_primes(end, start):
    lst = []
    for i in range(start, end + 1):
        for j in range(2, i):
            if i % j == 0:
                # если делитель найден, число не простое.
                break
        else:
            lst.append(i)
    print(f'конец выполнения {end, start}')
    return lst


threads = []
start = time.time()
thr = threading.Thread(target=find_primes, args=(10000,3))
thr.start()
threads.append(thr)
thr = threading.Thread(target=find_primes, args=(20000, 10001))
thr.start()
threads.append(thr)
thr = threading.Thread(target=find_primes, args=(30000, 20001))
thr.start()
threads.append(thr)
for thr in threads:
    thr.join()
print(f'время выполнения: {time.time() - start} сек')