# В одном потоке заполняем список, в другом - выводим длину этого списка
from threading import Thread, Event

lst = []


def print_len(my_ev):
    global lst
    if not my_ev.is_set():
        print('Doing some stuff')
        my_ev.wait()
    lst.remove('stop')
    print(f'length of {lst} is {len(lst)}')


if __name__ == '__main__':
    ev = Event()
    ev.clear()
    t = Thread(target=print_len, args=(ev,))
    t.start()
    while 'stop' not in lst:
        lst.append(input())
    ev.set()
    t.join()
