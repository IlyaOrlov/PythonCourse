import multiprocessing
import time


def add(*args):
    if isinstance(args[0], int):
        back = 0
    elif isinstance(args[0], float):
        back = 0
    elif isinstance(args[0], list):
        back = list()
    else:
        back = ' '
    start_time = time.time()
    for elem in args:
        back += elem
    print(back)
    print('Сложение для {}, затрачено {} sec.'.format(type(args[0]), time.time() - start_time))


if __name__ == '__main__':
    start_time = time.time()
    multiprocess = []
    p1 = multiprocessing.Process(target=add, args=(1, 2, 3, 4,))
    multiprocess.append(p1)
    p2 = multiprocessing.Process(target=add, args=(1.6, 2.7, 3.3, 5.4,))
    multiprocess.append(p2)
    p3 = multiprocessing.Process(target=add, args=('a', 'b', 'c', 'd',))
    multiprocess.append(p3)
    p4 = multiprocessing.Process(target=add, args=([1, 2, 3, 4], ['abcd'], [1.1, 2.2],))
    multiprocess.append(p4)
    for mp in multiprocess:
        mp.start()
        mp.join()

