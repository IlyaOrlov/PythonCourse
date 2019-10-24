import time


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

start = time.time()
find_primes(10000, 3)
find_primes(20000, 10001)
find_primes(30000, 20001)
print(f'время выполнения: {time.time() - start} сек')