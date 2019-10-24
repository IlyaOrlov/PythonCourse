import time
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


results = []
for i in range(3):
    start_time = time.time()
    find_primes(10000)
    find_primes(20000, 10001)
    find_primes(30000, 20001)
    results.append(time.time() - start_time)
    print('Всего затрачено времени при последовательном запуске: {0:3.2f} sec.'.format(time.time() - start_time))
with open('result.txt', 'a') as res:
    res.write('Normal: {0:3.2f} sec.\n'.format(np.mean(results)))

with open('result.txt', 'r') as res:
    text = res.read()
    if 'Normal' and 'Threading' and 'Multiprocessing' in text:
        for line in text.split('\n'):
            if str(min([float(elem) for elem in re.findall(r'\d+.\d+', text)])) in line:
                print('Best result: {}'.format(line))
