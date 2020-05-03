from threading import Thread
import multiprocessing as mp
import time

def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

def find_primes(inp, outp, named):
    list = []
    st_time = time.time()
    for each in range(inp, outp):
        if is_prime(each) == True:
            list.append(each)
    stop_time = time.time() - st_time
    print('instanse named {} work {} second'.format(named, stop_time))


if __name__ == '__main__':
    st = time.time()
    find_primes(3, 100000, "first_line")
    find_primes(10010, 20000, "second_line")
    find_primes(20010, 30000, "third_line")
    st: float = time.time() - st
    print(st)

    thread_list = [Thread(target=find_primes, args=(3, 10000, 'Threading1')),
                   Thread(target=find_primes, args=(10001, 20000, 'Threading2')),
                   Thread(target=find_primes, args=(20001, 30000, 'Threading3'))
                   ]
    
    st1 = time.time()
    for each in thread_list:
        each.start()

    for each in thread_list:
        each.join()
    st1: float = time.time() - st1
    print(st1)

    process_list = [mp.Process(target=find_primes, args=(3, 10000, 'Processing1')),
                    mp.Process(target=find_primes, args=(10001, 20000, 'Processing2')),
                    mp.Process(target=find_primes, args=(20001, 30000, 'Processing3'))
                    ]
    
    st2 = time.time()
    for each in process_list:
        each.start()
    for each in process_list:
        each.join()
    st2: float = time.time() - st2
    print(st2)

if st < st1 and st < st2:
    print('прямое выполнение функций самое быстрое')
elif st1 < st2 and st1 < st:
    print('потоковое выполнение самое быстрое')
else:
    print('мультипроцессорный метод самый быстрый')