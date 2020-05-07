import threading
import multiprocessing
import math
import time


def find_primes(start, end):
    list_numbers = []
    if start <= 2:
        list_numbers.append(2)
    for number in range(start, end):
        lim = math.ceil(math.sqrt(number))
        result = True
        for i in range(2, lim+1):
            if number % i == 0:
                result = False
                break
        if result:
            list_numbers.append(number)
    if 1 in list_numbers:
        del list_numbers[list_numbers.index(1)]
    return list_numbers


if __name__ == '__main__':
    print('Один поток')
    start = time.time()
    find_primes(3, 10000)
    find_primes(10001, 20000)
    find_primes(20001, 30000)
    time1 = time.time() - start
    print(f'Время операции: {time1}')


if __name__ == '__main__':
    print('Три потока')
    start = time.time()
    t1 = threading.Thread(target=find_primes, args=(3, 10000))
    t2 = threading.Thread(target=find_primes, args=(10001, 20000))
    t3 = threading.Thread(target=find_primes, args=(20001, 30000))
    threads = [t1, t2, t3]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    time2 = time.time() - start
    print(f'Время операции: {time2} ')
    print((time1 > time2))


if __name__ == '__main__':
    print('Три процесса')
    start = time.time()
    proc_1 = multiprocessing.Process(target=find_primes, args=(3, 10000))
    proc_2 = multiprocessing.Process(target=find_primes, args=(10001, 20000))
    proc_3 = multiprocessing.Process(target=find_primes, args=(20001, 30000))
    processes = [proc_1, proc_2, proc_3]

    for proc in processes:
        proc.start()

    for proc in processes:
        proc.join()

    time3 = time.time() - start
    print(f'Время операции: {time3} ')
    print((time2 > time3))

