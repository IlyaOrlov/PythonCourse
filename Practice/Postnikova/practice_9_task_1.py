import threading
import time
import multiprocessing

#Task_1

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
all_threads = []
def find_primes_with_threads(values):
    start_1 = time.time()
    for i in range(3):
        for my_range in all_values:
            thr = threading.Thread(target=find_primes, args=my_range)
            thr.start()
            all_threads.append(thr)

    for thr in all_threads:
        thr.join()
        print('Thread {} is joined'.format(thr))
    thr_result = time.time() - start_1
    print('With threads it takes ' + '{0:.4f} sec'.format(thr_result))
    return thr_result


# Process
all_process = []
start_2 = time.time()
if __name__ == "__main__":
    thr_result = find_primes_with_threads(all_values)
    for j in range(3):
        for my_range in all_values:
            p = multiprocessing.Process(target=find_primes, args=my_range)
            p.start()
            all_process.append(p)

    for p in all_process:
        p.join()
        print('Process {} is joined'.format(p))
    p_result = time.time() - start_2
    print('With process it takes ' + '{0:.4f} sec'.format(p_result))

    '''Если забыть выполнить start(), то ни процесс, ни поток просто не запустятся, при наличии в коде join() далее выдаётся ошибка "RuntimeError: cannot join thread before it is started".'''
    '''Если забыть выполнить join() для треда, то работа приложения может завершится раньше, чем все треды завершат свою работу, а для процесса - основной процесс завершится, а процессы продолжат свою работу'''


    if (thr_result < p_result):
        print(f"Using threads is faster than process by {p_result-thr_result}")
    else:
        print(f"Using threads is faster than process by {thr_result - p_result} sec")

