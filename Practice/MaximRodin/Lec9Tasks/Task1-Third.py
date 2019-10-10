import time
import multiprocessing

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


    print('Результат поиска простых числе в диапазоне от {} до {}:'.format(start, end),res)
    print('Конец поиска простых чисел, затрачено {} sec.'.format(time.time() - start_time))


if __name__ == '__main__':
    restime = []
    for i in range(3):
        start_time = time.time()
        p1 = multiprocessing.Process(target=find_primes, args=(10000, 3))
        p2 = multiprocessing.Process(target=find_primes, args=(20000, 10001,))
        p3 = multiprocessing.Process(target=find_primes, args=(30000, 20001,))
        p1.start()
        p2.start()
        p3.start()
        p1.join()
        p2.join()
        p3.join()
        restime.append(time.time() - start_time)
        break