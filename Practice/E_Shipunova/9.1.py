import time
import threading
from multiprocessing import Process


def find_primes(end, start=3):
    res = []
    for num in range(start, end + 1):
        for i in range(2, num):  # don't take num, because all num % num == 0
            if num % i == 0:
                break

            if i == num - 1:
                res.append(num)

    return res


if __name__ == "__main__":

    # The first option - sequential execution of threads
    start_seq = time.perf_counter()
    find_primes(10000)
    find_primes(20000, 10001)
    find_primes(30000, 20001)
    print(f'The sequential execution takes {round(time.perf_counter() - start_seq, 4)} sec by sequential threads.')

    # The second option - parallel execution of threads (1)
    start2 = time.perf_counter()
    our_args = [[10000], [20000, 10001], [30000, 20001]]
    threads = []

    for i in range(len(our_args)):
        thr = threading.Thread(target=find_primes, args=(*our_args[i],))
        start_par = time.perf_counter()
        thr.start()
        threads.append(thr)

    for thr in threads:
        thr.join()
    print(f'The parallel execution takes {round(time.perf_counter() - start2, 4)} sec by parallel threads.')

    # The third option - parallel execution of processes (2)
    start3 = time.perf_counter()
    processes = []
    for i in range(len(our_args)):
        p = Process(target=find_primes, args=(*our_args[i],))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
    print(f'The parallel execution takes {round(time.perf_counter() - start3, 4)} sec by parallel processes.')

'''
1. Рассмотрим запуск ф-ции в ||-ных потоках (1):
   - если "забыть" .start(), а .join() оставить,
     то созданные потоки не будут запущены на выполнение, а когда выполнение любого потока дойдет до
     строки с .join() - то будет выброшено исключение "RuntimeError: cannot join thread before it is started",
     что вполне логично, выполнение программы закончится аварийно;
   - если "забыть" .join(), а .start() оставить,
     то потоки будут созданы, запущены на выполнение параллельно с работой главного потока, который завершит
     свое выполнение в нашем случае раньше, чем "отработают" запущенные потоки. Но это не приведет к "гибели"
     дочерних потоков, они корректно "отработают" свои инструкции;
   - если "забыть" .join() и .start(), то "отработает" только главный поток, параллельные потоки будут созданы,
     но ни запуска, ни завершения выполнено не будет.

2. Рассмотрим запуск ф-ции в ||-ных процессах (2):
   - если "забыть" .start(), а .join() оставить, то созданные процессы не будут запущены на выполнение, а именно
     им не будет присвоен атрибут 'wait', что также в строке с .join() приведет к исключению, но уже типа
     "AttributeError: 'NoneType' object has no attribute 'wait'", что приведет к аварийному завершению программы;
   - если "забыть" .join(), а .start() оставить, получим ситуацию полностью идентичную ситуации с потоками:
     процессы будут созданы, запущены на выполнение параллельно с работой главного процесса, который завершит
     свое выполнение раньше, чем "отработают" дочернии процессы. Но это не приведет к "гибели" дочерних процессов,
     они корректно "отработают" свои инструкции;
   - если "забыть" .join() и .start(), вновь полная аналогия с потоками: "отработает" только главный процесс,
     параллельные процессы будут созданы, но ни запуска, ни завершения выполнено не будет.

Выводы (сравнение результатов):
    "The sequential execution takes 5.9971 sec by sequential threads.
     The parallel execution takes 5.8631 sec by parallel threads.
     The parallel execution takes 4.6644 sec by parallel processes."

       Как видно из output, времена выполнения 3-х запусков ф-ции find_primes() в последовательных и параллельных потоках
    соизмеримы, и ожидаемого "выйгрыша" от запуска кода в параллельных потоках не получено, что обусловлено наличием
    в python GIL - доступ к интерпритатору в единый момент времени имеет лишь 1 поток, что приводит к невозможности,
    а соответственно и нецелесообразности использования ||-ных потоков (даже расточительного использования ресурсов за
    счет создания для каждого потока своего стека).

       Выполнение 3-х запусков ф-ции find_primes() в параллельных процессах занимает наименьшее время, и соответственно
    более предпочтительно для решения подобных задач.

'''
