import time
import multiprocessing


def find_primes(start, end):
    primes = []
    start_time = time.time()
    for num in range(start, end + 1):
        if num > 1:
            for n in range(2, num):
                if (num % n) == 0:
                    break
            else:
                primes.append(num)
    print(f"Calculating prime numbers from {start} to {end}, finished in {time.time() - start_time} sec.")
    return primes


starts = [3, 10001, 20001]
ends = [10000, 20000, 30000]

if __name__ == '__main__':
    start_process = time.time()
    processes = []
    for i in range(3):
        process = multiprocessing.Process(target=find_primes, args=(starts[i], ends[i]))
        process.start()
        processes.append(process)
        process.join()
    print(f"Multiprocessing computing time: {time.time() - start_process} sec.")
