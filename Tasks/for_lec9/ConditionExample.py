from threading import Thread, Condition
import time

lst = []


def print_fun(cv):
    global lst
    while True:
        with cv:
            while len(lst) == 0:
                cv.wait()
            if 'q' in lst:
                cv.notify()
                break
            while len(lst) > 0:
                print(lst.pop(0),)
            cv.notify()
            time.sleep(1)


if __name__ == '__main__':
    cv = Condition()
    lst.append(input())
    t = Thread(target=print_fun, args=(cv,))
    t.start()
    while True:
        with cv:
            while len(lst) > 0 and 'q' not in lst:
                cv.wait()
            lst.append(input())
            cv.notify()
            if 'q' in lst:
                break
            time.sleep(1)
    t.join()
