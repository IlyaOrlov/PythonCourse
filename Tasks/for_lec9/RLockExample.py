from threading import Thread, RLock
import time

a = None


def print_fun(lock):
    global a
    while True:
        lock.acquire()
        if a:
            if a == 'q':
                lock.release()
                break
            print(a, end=' ')
            a = None


if __name__ == '__main__':
    lock = RLock()
    a = input()
    t = Thread(target=print_fun, args=(lock,))
    t.start()
    while True:
        if a == 'q':
            break
        lock.acquire()
        a = input()
        lock.release()
        time.sleep(1)
    t.join()
