from multiprocessing import Pool
import time
import os

only_my_data = []


def fun(data):
    only_my_data.append(data)
    print(f'My PID is {os.getpid()}. I have this data: {only_my_data}')
    time.sleep(1)
    return data


if __name__ == "__main__":
    pool = Pool(processes=3)
    big_data = [1, 2, "three", [4, 4, 4, 4], "five", 6, "seven"]
    res = pool.map(fun, big_data)

    print(res)
