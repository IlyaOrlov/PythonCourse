import threading
import random


def private_func(d):
    try:
        num = d.num
    except AttributeError:
        print('Private info is not set for the {}'.format(threading.current_thread().name))
    else:
        print('Private info number {} is set for the {}'.format(num, threading.current_thread().name))


def func(d):
    private_func(d)
    d.num = random.randint(10000, 99999)
    private_func(d)


if __name__ == '__main__':
    d = threading.local()
    for i in range(5):
        my_thread = threading.Thread(target=func, args=(d,))
        my_thread.start()
