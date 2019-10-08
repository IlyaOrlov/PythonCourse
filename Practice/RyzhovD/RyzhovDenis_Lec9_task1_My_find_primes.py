'''
Lec9_ex1
Calculate prime numbers in three subsequent ranges:
[3-10**POWER]; [1-2]*10**POWER; [2-3]*10**POWER
in
s) serial mode
t) threading mode
m) multiprocessing mode
'''

import threading
import multiprocessing
import time
from numpy import sqrt

POWER = 4

def my_find_primes(end, start=3):
    start_clock = time.time()
    prime_list = []
    for n in range(start, end):
        flag = 0
        for k in range(2,int(sqrt(n))+1):
            if n%k == 0:
                flag = +1
        if flag == 0:
            prime_list.append(n)

    tau = int((10**6)*(time.time()-start_clock))/1000

    print('Calculations of prime numbers from {} to {} took {} ms.'
          .format(start, end, tau))
    return prime_list, tau

### SERIES
print('> SERIES <')
start_clock = time.time()
a1, tau1 = my_find_primes(10**POWER)
a2, tau2 = my_find_primes(2*10**POWER, 10**POWER+1)
a3, tau3 = my_find_primes(3*10**POWER, 2*10**POWER+1)

tau_s = int((10**6)*(time.time()-start_clock))/1000
print('---')
print('Calculations of prime numbers in given range as a series '
      'took {} ms.\n'.format(tau_s))
# ts = []
# ts.append(tau_s)



### THREADING
print('> THREADING <')
start_clock = time.time()

threads = []
for j in range(3):
    if j == 0:
        start = 3
    else:
        start = j*(10**POWER)+1
    end = (j+1)*(10**POWER)
    # create an object of threading
    thr = threading.Thread(target= my_find_primes, args=(end, start))  # creation of thread
    thr.start()  # [cap] start of the current thread
    threads.append(thr)

for thr in threads:
    thr.join()  #  the program waits for completion of each thread

# The question is: How to read the result of executing of each thread?

tau_th = int((10**6)*(time.time()-start_clock))/1000
print('---')
print('Calculations of prime numbers in given range in threading mode '
      'took {} ms.\n'.format(tau_th))

### MULTIPROCESSING
print('> MULTIPROCESSING <')
start_clock = time.time()
processes = []
if __name__ == '__main__': # NECESSARY!
    process = []
    for j in range(3):
        if j == 0:
            start = 3
        else:
            start = j * (10 ** POWER) + 1
        end = (j + 1) * (10 ** POWER)
        # create an object of threading
        prc = multiprocessing.Process(target=my_find_primes, args=(end, start))
        prc.start()
        processes.append(prc)

    for prc in processes:
        prc.join()

    tau_mp = int((10 ** 6) * (time.time() - start_clock)) / 1000
    print('---')
    print('Calculations of prime numbers in given range in multiprocessing mode '
          'took {} ms.\n'.format(tau_mp))


### TEST
# print(a1)
# print('')
# print(a2)
# print('')
# print(a3)
# print('')