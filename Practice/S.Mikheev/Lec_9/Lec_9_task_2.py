import time
import multiprocessing


def adder(*args):
    if isinstance(args[0], list):
        output = list()
    elif isinstance(args[0], int) or isinstance(args[0], float):
        output = 0
    else:
        output = ''
    start_time = time.time()
    print('Начало вычислений')
    for elem in args:
        output += elem
    print(output)
    print('Конец операции сложения для типа {}, затрачено {} sec.'.format(type(args[0]), time.time() - start_time))


if __name__ == '__main__':  # обязательно для многопроцессного приложения
    start_time = time.time()
    multiprocess = []
    p1 = multiprocessing.Process(target=adder, args=('aaa', 'bbbb', 'cccc', 'dddd',))
    multiprocess.append(p1)
    p2 = multiprocessing.Process(target=adder, args=(1, 2, 3, 4,))
    multiprocess.append(p2)
    p3 = multiprocessing.Process(target=adder, args=(5.5, 7.8, 3.4, 5.6,))
    multiprocess.append(p3)
    p4 = multiprocessing.Process(target=adder, args=([1, 2, 3, 4, 5], [10, 55, 77, 89], ['asd', 'rrr'], [12.3, 13.2],))
    multiprocess.append(p4)
    for mp in multiprocess:
        mp.start()
        mp.join()
    print('Общее время вычислений в секундах: {}'.format(int(time.time() - start_time)))
