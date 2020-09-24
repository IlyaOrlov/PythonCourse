import threading
import time
import multiprocessing


# Task_1

# Threads
def find_primes(end, start=3):
    simple_numbers = []
    for i in range(start, end + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            simple_numbers.append(i)
    print(f"In range from {start} to {end} I have found {len(simple_numbers)} primes")
    return simple_numbers


all_values = [(10000, 3), (20000, 10001), (30000, 20001)]


def find_primes_with_threads():
    print('Start measuring with threads')
    start = time.time()
    all_threads = []
    for my_range in all_values:
        thr = threading.Thread(target=find_primes, args=my_range)
        thr.start()
        all_threads.append(thr)

    for thr in all_threads:
        thr.join()
        print('Thread {} is joined'.format(thr))
    thr_result = time.time() - start
    print('With threads it takes ' + '{0:.4f} sec'.format(thr_result))
    return thr_result


# Process
all_process = []
if __name__ == "__main__":
    thr_result = find_primes_with_threads()

    print('Start measuring in sequence run')
    start = time.time()
    for my_range in all_values:
        find_primes(*my_range)
    result_without_thr_and_p = time.time() - start
    print('Without threads and processes it takes ' + '{0:.4f} sec'.format(result_without_thr_and_p))

    print('Start measuring with processes')
    start = time.time()
    for my_range_1 in all_values:
        p = multiprocessing.Process(target=find_primes, args=my_range_1)
        p.start()
        all_process.append(p)

    for p in all_process:
        p.join()
        print('Process {} is joined'.format(p))
    p_result = time.time() - start
    print('With process it takes ' + '{0:.4f} sec'.format(p_result))

    """Если забыть выполнить start(), то ни процесс, ни поток просто не запустятся, 
    при наличии в коде join() далее выдаётся ошибка "RuntimeError: cannot join thread before it is started".
    
    Если забыть выполнить join() для треда, то работа приложения может завершится раньше, 
    чем все треды завершат свою работу, а для процесса - основной процесс завершится, 
    а процессы продолжат свою работу"""

    if thr_result < p_result and thr_result < result_without_thr_and_p:
        print(f"Using threads is faster than processes by {p_result - thr_result} sec "
              f"and sequential start by {p_result - result_without_thr_and_p} sec")
    elif thr_result > p_result and result_without_thr_and_p > p_result:
        print(f"Using processes is faster than threads by {thr_result - p_result} sec "
              f"and than sequential start by {result_without_thr_and_p - p_result} sec")
    elif result_without_thr_and_p < thr_result and result_without_thr_and_p < p_result:
        print(f"Using sequential start is faster than threads by {thr_result - result_without_thr_and_p} sec "
              f"and than processes by {p_result - result_without_thr_and_p} sec")

"""Итог: Using processes is faster than threads by 1.7642529010772705 sec and than sequential start by 1.0940639972686768 sec, - таким образом, для вычислений 
использование threads не слишком эффективно, поскольку требует дополнительных ресурсов на создание потоков и переключение между потоками, что занимает дополнительное время.
Кроме того, поскольку интерпретатор CPython не является поткобезопасным, в нём используется блокровка Global Interpreter Lock (GIL), которая разрешает в каждый момент времени
выпонлять байт-код только одному потоку, т.е. добиться параллелизма при использовании потоков невозможно.
Следовательно, самый быстрый результат для выполнения существенного объёма вычислений даёт использование процессов."""