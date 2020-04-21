from threading import Thread, Event
import time

lst = []


def print_fun(ev):
    global lst
    while True:
        if ev.is_set():
            ev.wait()
            if 'q' in lst:
                break
            while len(lst) > 0:
                print(lst.pop(0),)
        time.sleep(1)  # делает возможным, но не гарантирует переключение на другой поток


if __name__ == '__main__':
    ev = Event()
    t = Thread(target=print_fun, args=(ev,))
    lst.append(input())
    ev.set()  # lst не пустой, поэтому разрешаем чтение из lst
    t.start()
    while True:
        if 'q' in lst:
            break
        ev.clear()
        lst.append(input())
        ev.set()
        time.sleep(1)  # делает возможным, но не гарантирует переключение на другой поток
    t.join()
