# В одном потоке заполняем список, в другом - выводим длину этого списка
from threading import Thread

lst = []


def print_len():
    global lst
    # while True:
    if 'stop' in lst:
        lst.remove('stop')
        print(f'length of {lst} is {len(lst)}')


if __name__ == '__main__':
    t = Thread(target=print_len)
    t.start()
    while 'stop' not in lst:
        lst.append(input())
    t.join()
