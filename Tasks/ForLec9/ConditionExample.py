from threading import Thread, Condition
import time

a = None


def print_fun(cv):
    global a
    while True:
        with cv:
            while not a:
                cv.wait()
            if a == 'q':
                cv.notify()
                break
            print(a,)
            a = None
            cv.notify()


if __name__ == '__main__':
    cv = Condition()
    a = input()
    t = Thread(target=print_fun, args=(cv,))
    t.start()
    while True:
        with cv:
            while a and a != 'q':
                cv.wait()
            if a == 'q':
                break
            a = input()
            cv.notify()
            time.sleep(5)
    t.join()
