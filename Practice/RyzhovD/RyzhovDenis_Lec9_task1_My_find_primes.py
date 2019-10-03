'''
Lec9_ex1
Calculate prime numbers in three subsequent ranges:
[3-10**POWER]; [1-2]*10**POWER; [2-3]*10**POWER
in
s) serial mode
t) threading mode
m) multiprocessing mode

Code works, but results seems to be strange:
POWER = 4
Average total time of serial process: 176.706 ms.
Average total time of threading process): 187.327 ms.
Average total time of multiprocessing process: 212.221 ms.
POWER = 5
Total time of processes [serial, threading, multiprocessing]: [5762.488, 5624.488, 5521.745] ms.

There are no gain for threading and multiprocessing modes.
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

## series
start_clock = time.time()
a1, tau1 = my_find_primes(10**POWER)
a2, tau2 = my_find_primes(2*10**POWER, 10**POWER+1)
a3, tau3 = my_find_primes(3*10**POWER, 2*10**POWER+1)

tau_s = int((10**6)*(time.time()-start_clock))/1000
print('===')
print('Calculations of prime numbers in given range as a series '
      'took {} ms.\n'.format(tau_s))
# ts = []
# ts.append(tau_s)



### THREADING

start_clock = time.time()
threads = []
a_j = []
tau_j = []

for j in range(3):
    if j == 0:
        start = 3
    else:
        start = j*(10**POWER)+1
    end = (j+1)*(10**POWER)
    # create an oject of threading
    thr = threading.Thread(target= my_find_primes, args=(end, start))
    thr.start()
    threads.append(thr)

for thr in threads:
    thr.join()
## ?? a_j[j], tau_j[j] = My_find_primes()
tau_th = int((10**6)*(time.time()-start_clock))/1000
print('  |||')
print('Calculations of prime numbers in given range in threading mode '
      'took {} ms.\n'.format(tau_th))



### MULTIPROCESSING

start_clock = time.time()
if __name__ == '__main__': # NECESSARY!
    process = []
    for j in range(3):
        if j == 0:
            start = 3
        else:
            start = j * (10 ** POWER) + 1
        end = (j + 1) * (10 ** POWER)
        # create an oject of threading
        prc = multiprocessing.Process(target=my_find_primes, args=(end, start))
        prc.start()
        prc.join()

    ## ?? a_j[j], tau_j[j] = My_find_primes()
    tau_mp = int((10 ** 6) * (time.time() - start_clock)) / 1000
    print('  ***')
    print('Calculations of prime numbers in given range in multiprocessing mode '
          'took {} ms.\n'.format(tau_mp))


### TEST
# print(a1)
# print('')
# print(a2)
# print('')
# print(a3)
# print('')

### HANDMADE SAVE
t4_ser = [[38.975, 61.768, 77.713, 178.594],
         [39.921, 61.857, 73.547, 175.467],
         [38.971, 60.027, 76.957, 176.059]]

t4_th = [[105.646, 146.307, 158.856, 184.587],
         [86.617, 157.078, 163.18, 181.107],
         [116.844, 172.79, 161.78, 196.288]]

t4_mp = [[43.55, 71.69, 82.377, 235.067],
         [39.915, 63.726, 80.431, 196.319],
         [43.524, 66.53, 86.126, 205.28]]

t5 = [[1003.059, 2164.494, 2594.785, 5762.488],
      [3003.411, 4746.152, 5593.576, 5624.488],
      [989.08, 1891.737, 2629.82, 5521.745]]

t4_ser_tot = (t4_ser[0][3] + t4_ser[1][3] + t4_ser[2][3])/3
t4_th_tot = (t4_th[0][3] + t4_th[1][3] + t4_th[2][3])/3
t4_mp_tot = (t4_mp[0][3] + t4_mp[1][3] + t4_mp[2][3])/3
print('=== data for runtime ===')
print('POWER = 4')
print('Average total time of serial process: {} ms.'
      .format(int(t4_ser_tot*1000)/1000))
print('Average total time of threading process): {} ms.'
      .format(int(t4_th_tot*1000)/1000))
print('Average total time of multiprocessing process: {} ms.'
      .format(int(t4_mp_tot*1000)/1000))
print('POWER = 5')
print('Total time of processes [serial, threading, multiprocessing]: [{}, {}, {}] ms.'
      .format(int(t5[0][3]*1000)/1000, int(t5[1][3]*1000)/1000, int(t5[2][3]*1000)/1000))