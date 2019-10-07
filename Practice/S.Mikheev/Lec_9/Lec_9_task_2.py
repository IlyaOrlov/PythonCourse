import time
import multiprocessing


def adder(*args):
    flag = type(args[0])
    a_num = 0
    a_str = ''
    start_time = time.time()
    print('Начало вычислений')
    for elem in args:
        if flag is int or flag is float:
            a_num += elem
        else:
            a_str += elem
    if flag is int or flag is float:
        print(a_num)
    else:
        print(a_str)
    print('Конец операции сложения для типа {}, затрачено {} sec.'.format(flag, time.time() - start_time))


if __name__ == '__main__':  # обязательно для многопроцессного приложения
    start_time = time.time()
    p1 = multiprocessing.Process(target=adder, args=('aaa', 'bbbb', 'cccc', 'dddd',))
    p2 = multiprocessing.Process(target=adder, args=(1, 2, 3, 4,))
    p3 = multiprocessing.Process(target=adder, args=(5.5, 7.8, 3.4, 5.6,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print('Общее время вычислений в секундах: {}'.format(int(time.time() - start_time)))
