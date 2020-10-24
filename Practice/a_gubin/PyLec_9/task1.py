from threading import Thread
from multiprocessing import Process
import time


def find_prime(start, stop):
    primes = []

    def is_prime(number):
        for divider in range(2, number):
            if not number % divider:
                return False
        return True

    for number in range(start, stop):
        if is_prime(number):
            primes.append(number)

    return primes


def timer_dec(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        return time.time() - start_time
    return wrapper


@timer_dec
def single_thread_way(diapasons):
    for diapason in diapasons:
        find_prime(*diapason)


@timer_dec
def multi_thread_way(diapasons):
    threads = [Thread(target=find_prime, args=(*diapason,)) for diapason in diapasons]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


@timer_dec
def multi_process_way(diapasons):
    processes = [Process(target=find_prime, args=(*diapason,)) for diapason in diapasons]
    for process in processes:
        process.start()
    for process in processes:
        process.join()


if __name__ == "__main__":
    diapasons = [(3, 10000), (10001, 20000), (20001, 30000)]
    print(f"Single thread computing took {single_thread_way(diapasons)} sec")
    print(f"Multi thread computing took {multi_thread_way(diapasons)} sec")
    print(f"Multi process computing took {multi_process_way(diapasons)} sec")
