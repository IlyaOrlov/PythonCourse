import time
import multiprocessing
import numpy as np
import re


def find_primes(end, start=3):
    start_time = time.time()
    print('Начало поиска простых чисел в диапазоне от {} до {}'.format(start, end))
    a = []
    for elem in range(start, end):
        flag = True
        for i in range(2, elem // 2 + 1):
            if elem % i == 0:
                flag = False
                break
        if flag:
            a.append(elem)

    print('Конец поиска простых чисел в диапазоне от {} до {}, затрачено {} sec.'.format(start, end,
                                                                                         time.time() - start_time))
    return a


if __name__ == '__main__':  # обязательно для многопроцессного приложения
    results = []
    for i in range(3):
        start_time = time.time()
        p1 = multiprocessing.Process(target=find_primes, args=(10000,))
        p2 = multiprocessing.Process(target=find_primes, args=(20000, 10001,))
        p3 = multiprocessing.Process(target=find_primes, args=(30000, 20001,))
        p1.start()
        p2.start()
        p3.start()
        p1.join()
        p2.join()
        p3.join()
        results.append(time.time() - start_time)
        print(
            'Всего затрачено времени при поиске каждого диапазона в отдельном процессе с помощью '
            'multiprocessing.Process: {0:3.2f} sec.'.format(time.time() - start_time))
    with open('result.txt', 'a') as res:
        res.write('Multiprocessing: {0:3.2f} sec.\n'.format(np.mean(results)))

    with open('result.txt', 'r') as res:
        text = res.read()
        if 'Normal' and 'Threading' and 'Multiprocessing' in text:
            for line in text.split('\n'):
                if str(min([float(elem) for elem in re.findall(r'\d+.\d+', text)])) in line:
                    print('Best result: {}'.format(line))

