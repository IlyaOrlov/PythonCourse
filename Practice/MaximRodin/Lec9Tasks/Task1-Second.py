import time
import threading

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


restime = []
for i in range(3):
    start_time = time.time()
    threads = []
    my_thr = threading.Thread(target=find_primes, args=(10000, 3))
    my_thr.start()
    threads.append(my_thr)
    my_thr = threading.Thread(target=find_primes, args=(20000, 10001,))
    my_thr.start()
    threads.append(my_thr)
    my_thr = threading.Thread(target=find_primes, args=(30000, 20001,))
    my_thr.start()
    threads.append(my_thr)

    for my_thr in threads:
        my_thr.join()
    restime.append(time.time() - start_time)
    print('Всего затрачено времени с помощью threading.Thread: {} sec'.format(time.time() - start_time))


    break