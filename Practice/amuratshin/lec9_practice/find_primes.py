import threading
import multiprocessing
import time


def find_primes(start_n, end_n):
    # нахождение простого числа, которое делиться толко на себя и на еденицу
    for i in range(start_n, end_n):
        for x in range(2, i):
            # для каждого числа i из диапозона от start до end
            if i % x == 0:
                # проверяется условие (остаток от деления равен 0) начиная от 2 до самого числа i
                break
                # прерываем если условие соблюдено и переходим к else
        else:
            print(i)


# Запустить последовательно для каждого диапозона
#  ___Общее время вычислений в секундах: 5.00
# start = time.perf_counter()
# find_primes(3, 10000)
# find_primes(10001, 20000)
# find_primes(20001, 30000)
# print('Общее время вычислений в секундах: {0:.2f}'.format(int(time.perf_counter() - start)))


# Запустить ее три раза с теми же аргументами, но каждый раз в отдельном потоке с помощью threading.Thread.
# ___Общее время вычислений в секундах: 2.23 (Если запускать и прерывать процесс до запуска последующего)
#                                       2.26 (Если запускать все процессы и только потом начинать их прерывать)
#                                       2.13 (Если не прерывать, не джойнить запущенные процессы)
start = time.perf_counter()
pr1 = threading.Thread(name='th1_d1', target=find_primes(3, 10000))
pr2 = threading.Thread(name='th1_d1', target=find_primes(3, 10000))
pr3 = threading.Thread(name='th1_d1', target=find_primes(3, 10000))
pr1.start()
pr2.start()
pr3.start()
# pr1.join()
# pr2.join()
# pr3.join()
print('Общее время вычислений в секундах: {0:.2f}'.format(time.perf_counter() - start))
# Если пытаться приостановить не запущенный поток
#   будет исключение "RuntimeError: cannot join thread before it is started"
# Если поток запущен но после этого не вызван join для прерывания
#   то никаких ошибок не будет


# Запустить ее три раза с теми же аргументами, но каждый раз в отдельном процессе с помощью multiprocessing.Process.
# ___Общее время вычислений в секундах: 2.55 (Если запускать и прерывать процесс до запуска последующего)
#                                       2.36 (Если запускать все процессы и только потом начинать их прерывать)
#                                       2.17 (Если не прерывать, не джойнить запущенные процессы)
# if __name__ == '__main__': # обязательно для многопроцессного приложения
#     start = time.perf_counter()
#     pr1 = multiprocessing.Process(target=find_primes(3, 10000))
#     pr2 = multiprocessing.Process(target=find_primes(3, 10000))
#     pr3 = multiprocessing.Process(target=find_primes(3, 10000))
#     pr1.start()
#     pr2.start()
#     pr3.start()
#     # pr1.join()
#     # pr2.join()
#     # pr3.join()
#     print('Общее время вычислений в секундах: {0:.2f}'.format(time.perf_counter() - start))