from multiprocessing import Pool
import time
import os


lst = []
def cube(x):
    lst.append(x)
    print(f"This process {os.getpid()} processed values {lst}")
    time.sleep(2)
    return x**3

if __name__ == '__main__':
    pool = Pool(processes=5)
    res = pool.map(cube, range(1,7))
    print(res)
