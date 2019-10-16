import time
import multiprocessing

args = [(10000, 3), (20000, 10001), (30000, 20001)]


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
    processes = []
    for arg in args:
        p = multiprocessing.Process(target=find_primes, args=arg)
        p.start()
        processes.append(p)
    for i in processes:
        i.join()

print(f'время выполнения: {time.time() - start}')
