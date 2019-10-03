from threading import Thread, Event
import time

a = None


def print_fun(ev):
    global a
    while True:
        if not ev.is_set():
            ev.set()
            if a:
                if a == 'q':
                    ev.clear()
                    break
                print(a,)
                a = None
            ev.clear()


if __name__ == '__main__':
    ev = Event()
    ev.set()
    a = input()
    ev.clear()
    t = Thread(target=print_fun, args=(ev,))
    t.start()
    while True:
        if a == 'q':
            break
        ev.set()
        a = input()
        ev.clear()
        time.sleep(5)
    t.join()
