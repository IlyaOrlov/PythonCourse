import time
import multiprocessing


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

if __name__ == '__main__':
    start = time.time()
    p1 = multiprocessing.Process(target=find_primes, args=(10000,3))
    p2 = multiprocessing.Process(target=find_primes, args=(20000, 10001))
    p3 = multiprocessing.Process(target=find_primes, args=(30000, 20001))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print(f'время выполнения: {time.time() - start}')