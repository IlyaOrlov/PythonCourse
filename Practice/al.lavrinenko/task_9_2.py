import multiprocessing
import random
import string
import time


def sum_all(*args):
    elem_type = type(args[0])
    if not all(isinstance(arg, elem_type) for arg in args):
        raise TypeError('All arguments must be of the same type')

    if isinstance(args[0], int):
        return sum(args)
    elif isinstance(args[0], str):
        return ''.join(args)
    elif isinstance(args[0], list):
        lst = []
        for arg in args:
            lst += arg
        return lst
    else:
        raise TypeError('Only integers, strings or lists are appropriate')


if __name__ == '__main__':
    int_test = []
    str_test = []
    list_test = []
    for _ in range(100000):
        int_test.append(random.randint(1, 1000))
        str_test.append(''.join(random.choices(string.ascii_uppercase, k=random.randint(1, 10))))
        list_test.append([random.randint(1, 1000) for _ in range(random.randint(1, 10))])

    t = time.time()
    sum_all(int_test)
    sum_all(str_test)
    sum_all(list_test)
    print('Execution time: ', time.time() - t)

    t = time.time()
    processes = [multiprocessing.Process(target=sum_all, args=int_test),
                 multiprocessing.Process(target=sum_all, args=str_test),
                 multiprocessing.Process(target=sum_all, args=list_test)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    print('Multiprocessing execution time: ', time.time() - t)
