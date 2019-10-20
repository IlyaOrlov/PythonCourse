from threading import Thread, RLock
import time

class Base:
    x = 0
    y = 0


def print_fun(l):
    i = 0
    while i < 2:
        l.acquire()
        Base.x = input("2x: ")
        Base.y = input("2y: ")
        l.release()
        print(f'Thread 2: Base.x = {Base.x}, Base.y = {Base.y}')
        i += 1
        time.sleep(5)


if __name__ == '__main__':
    l = RLock()
    t = Thread(target=print_fun, args=(l,))
    t.start()
    i = 0
    while i < 2:
        l.acquire()
        Base.x = input("1x: ")
        Base.y = input("1y: ")
        l.release()
        print(f'Thread 1: Base.x = {Base.x}, Base.y = {Base.y}')
        i += 1
        time.sleep(5)
t.join()