import threading
import time
from multiprocessing import Process


def find_primes(start, stop):
     lst = []
     for i in range(start, stop + 1, 2):
          if i > 10 and i % 10 == 5:
               continue

          for j in lst:
               if j * j - 1 > i:
                    lst.append(i)
                    break
               if i % j == 0:
                    break
          else:
               lst.append(i)

     return lst


if __name__ == '__main__':
     numbers = {3: 10000, 10001: 20000, 20001: 30000}

     start_t1 = time.perf_counter()
     for i, k in numbers.items():
          find_primes(i, k)
     print(f'Running time in {round(time.perf_counter() - start_t1, 4)} seconds')

     start_t2 = time.perf_counter()
     lst_thr = []
     for j, t in numbers.items():
         thread = threading.Thread(target=find_primes, args=(j, t))
         thread.start()
         lst_thr.append(thread)

     for thread in lst_thr:
          thread.join()
     print(f'Running time threading in {round(time.perf_counter() - start_t2, 4)} seconds')

     """ Если исключить thread.start(), потоки создадутся но не будут запушены на выполнение,
         в конечном результате получим исключение RuntimeError: cannot join thread before it is started.
         Если исключить thread.join(), потоки создадутся и будут запущены, но главный поток выполнится раньше 
         чем запущенные.  
     """
     start_t3 = time.perf_counter()
     lst_pro = []
     for m, n in numbers.items():
          proc = Process(target=find_primes, args=(m, n))
          proc.start()
          lst_pro.append(proc)

     for proc in lst_pro:
          proc.join()
     print(f'Running time multiprocessing in {round(time.perf_counter() - start_t3, 4)} seconds')


     """ Если исключить thread.start(), процессы создадутся но не будут запушены на выполнение,
         в конечном результате получим и исключение AssertionError: can only join a started process.
         Если исключить thread.join(), процессы создадутся и будут запущены, но главный процесс выполнится раньше 
         чем запущенные.  
     
     Если вычисление функции find_primes занимает мало времини, следовательно потоки за счет конкуренции и GIL(который
     отдает полный доступ и позволяет выполнять операции только одному потоку) последовательное выполнение будет быстрее,
     чем создание процессов, а значит threading отработает быстрее всех и показывает лучший результат. 
     Но, если вычисление функции find_primes занимает большое время, то процессы за счет параллелизма выполнят вычисление
     быстрее, чем потоки и главный поток, потому-что, потоки не могут использовать параллелизм, а значит multiprocessing 
     отработает быстрее всех и показывает лучший результат. 
     """