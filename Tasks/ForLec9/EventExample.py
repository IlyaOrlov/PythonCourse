from threading import Thread, Event
import time

a = None


def print_fun(ev):
    global a
    while True:
        if ev.is_set():
            ev.clear()
            if a is not None:
                if a == 'q':
                    ev.set()
                    break
                else:
                    print(a,)
                    a = None
            ev.set()


if __name__ == '__main__':
    ev = Event()
    a = input()
    ev.set()
    t = Thread(target=print_fun, args=(ev,))
    t.start()
    while True:
        if a == 'q':
            break
        elif a is None:
            if ev.is_set():
                ev.clear()
                a = input()
                ev.set()
        time.sleep(5)
    t.join()
