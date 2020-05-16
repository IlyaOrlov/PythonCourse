import time
from threading import Thread
import multiprocessing


def fun(start, end):
    lst = []
    for n in range(start, end + 1):
        if n > 1:
            for x in range(2, n):
                if (n % x) == 0:
                    break
            else:
               lst.append(n)

    return lst


if __name__ == "__main__":

    start_time = time.time()
    fun(3, 10000)
    fun(10001, 20000)
    fun(20001, 30000)
    time1 = time.time() - start_time
    print("Один поток выполняет за ", time1)




    start_time = time.time()
    thread_lst = [Thread(target=fun, args=(3, 10000)),
                  Thread(target=fun, args=(10001, 20000)),
                  Thread(target=fun, args=(20001, 30000)),]
    for t in thread_lst:
        t.start()
    for t in thread_lst:
        t.join()
    time2 = time.time() - start_time
    print("Три потока выполняет за ", time2)
    print(time1 > time2)


    start_time = time.time()
    process_lst = [multiprocessing.Process(target=fun, args=(3, 10000)),
                  multiprocessing.Process(target=fun, args=(10001, 20000)),
                  multiprocessing.Process(target=fun, args=(20001, 30000))]
    for p in process_lst:
        p.start()
    for p in process_lst:
        p.join()

    time3 = time.time() - start_time
    print("Три процесса выполняет за ", time3)
    print(time2 > time3)


