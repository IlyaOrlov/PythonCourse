from threading import Thread, RLock
import time

a = None


def print_fun(lock):
    while True:
        lock.acquire()
        global a
        if a is not None:
            if a == 'q':
                lock.release()
                break
            else:
                print(a, end=' ')
                a = None
        lock.release()


if __name__ == '__main__':
    lock = RLock()
    a = input()
    t = Thread(target=print_fun, args=(lock,))
    t.start()
    while True:
        if a == 'q':
            break
        elif a is None:
            lock.acquire()
            a = input()
            lock.release()
        time.sleep(5)
    t.join()
