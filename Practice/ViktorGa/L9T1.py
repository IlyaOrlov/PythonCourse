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
work_time = time.time() - start_time
print(work_time)

start_time = time.time()
threads = [threading.Thread(target=find_primes, args=(3, 10000)),
           threading.Thread(target=find_primes, args=(10001, 20000)),
           threading.Thread(target=find_primes, args=(20001, 30000))]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
work_time = time.time() - start_time
print(work_time)
#Если не сделать thread.start(), то не запустятяся потоки, выдает ошибку.
#Если не сделать thread.join(), то он неправильно посчитает время, т.к. уже не ждет завершения.

if __name__ == "__main__":

    start_time = time.time()
    processes = [multiprocessing.Process(target=find_primes, args=(3, 10000)),
                 multiprocessing.Process(target=find_primes, args=(10001, 20000)),
                 multiprocessing.Process(target=find_primes, args=(20001, 30000))]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    work_time = time.time() - start_time
    print(work_time)
#Если не сделать process.start(), то выдаст ошибку с атрибутом wait, не запустится.
#Если не сделать process.join(), то неправильно считает время, не дожидается завершения.
#Итого: последовательно 7.465 с, паралл. поток 6.484 с, паралл. проц 5.122 - процесс самый быстрый
