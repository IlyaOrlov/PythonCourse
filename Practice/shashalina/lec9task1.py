# -*- coding: utf8 -*-
# Написать функцию find_primes(end, start), которая ищет все простые числа в диапазоне от заданного числа start
# (по умолчанию 3) до заданного числа end. Далее необходимо: Запустить ее три раза последовательно в диапазоне
# от 3 до 10000, от 10001 до 20000, от 20001 до 30000. Запустить ее три раза с теми же аргументами, но каждый раз
# в отдельном потоке с помощью threading.Thread. Что будет, если 'забыть' выполнить start или join для потоков?
# Запустить ее три раза с теми же аргументами, но каждый раз в отдельном процессе с помощью multiprocessing.Process.
# Что будет, если 'забыть' выполнить start или join для процессов? Замерить время исполнения каждого варианта
# и сравнить результаты

from threading import Thread
from multiprocessing import Process
import time

lst_start_elem = [3, 10001, 20001]
lst_end_elem = [10000, 20000, 30000]

def find_primes(end, start=3):
    lst = []
    for i in range(end, start-1, -1):
        if isSimple(i) == True:
            lst.append(i)
    print(lst)
    return lst

def isSimple(num):
    for i in range (2, num-1):
        if num %i == 0:
           return False
    return True

if __name__ == '__main__':
    start_time_fun = time.time()
    for i in range(len(lst_start_elem)):
        find_primes(lst_end_elem[i], lst_start_elem[i])
    end_time_fun = time.time() - start_time_fun

    thds = []
    start_time_thd = time.time()
    for i in range(len(lst_start_elem)):
        thd = Thread(target=find_primes, args=(lst_end_elem[i], lst_start_elem[i]))
        thds.append(thd)
        thd.start()
    for thd in thds:
        thd.join()
    end_time_thd = time.time() - start_time_thd

    prcs = []
    start_time_prc = time.time()

    for i in range(len(lst_start_elem)):
        prc = Process(target=find_primes, args=(lst_end_elem[i], lst_start_elem[i]))
        prcs.append(prc)
        prc.start()
    for prc in prcs:
        prc.join()
        end_time_prc = time.time() - start_time_prc

    print(f"Время обработки при:\nпоследовательном запуске функций - {end_time_fun}")
    print(f"при запуске в потоках - {end_time_thd}")
    print(f"при запуске в процессах - {end_time_prc}")
