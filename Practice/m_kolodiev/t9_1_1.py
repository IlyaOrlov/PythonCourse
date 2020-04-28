import time
import threading


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

start_seq = time.time()
for i in range(3):
    find_primes(starts[i], ends[i])
print(f"Sequential computing time: {time.time() - start_seq} sec.")

start_thr = time.time()
threads = []
for i in range(3):
    thread = threading.Thread(target=find_primes, args=(starts[i], ends[i]))
    thread.start()
    threads.append(thread)
    thread.join()
print(f"Multithreading computing time: {time.time() - start_thr}")
