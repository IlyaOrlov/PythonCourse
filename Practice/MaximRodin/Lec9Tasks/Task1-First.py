import time


def find_primes(end,start):
    start_time = time.time()
    print('Поиск простых чисел от {} до {}'.format(start, end))
    res = []
    for elem in range(start, end):
        a = True
        for i in range(2, elem):
            if elem % i == 0:
                a = False
                break
        if a:
            res.append(elem)

    print('Конец поиска, затрачено {} sec.'.format(start, end, time.time() - start_time))
    print('Результат поиска:',res)


restime = []
for i in range(3):
    start_time = time.time()
    find_primes(10000, 3)
    find_primes(20000, 10001)
    find_primes(30000, 20001)
    restime.append(time.time() - start_time)
    print('Времени затрачено: {} sec.'.format(time.time() - start_time))
    break