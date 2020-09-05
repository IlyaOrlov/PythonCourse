# В одном потоке заполняем список, в другом - выводим длину этого списка
from threading import Thread, Condition

lst = []


def print_len(my_cv):
    global lst
    with my_cv:
        # my_cv.wait_for(lambda: 'stop' in lst)
        while 'stop' not in lst:
            my_cv.wait()
    lst.remove('stop')
    print(f'length of {lst} is {len(lst)}')


if __name__ == '__main__':
    cv = Condition()
    t = Thread(target=print_len, args=(cv,))
    t.start()
    while 'stop' not in lst:
        lst.append(input())
        with cv:
            cv.notify()
    t.join()
