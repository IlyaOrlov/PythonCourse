from threading import Thread, RLock
import time

a = None


def print_fun(l):
    while True:
        l.acquire()
        global a
        if a:
            if a == 'q':
                l.release()
                break
            print(a, end=' ')
            a = None
        l.release()


if __name__ == '__main__':
    l = RLock()
    a = input()
    t = Thread(target=print_fun, args=(l,))
    t.start()
    while True:
        if a == 'q':
            break
        l.acquire()
        a = input()
        l.release()
        time.sleep(5)
t.join()
