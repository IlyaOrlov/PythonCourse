from multiprocessing import Process
import time


def add(*args):
    start_time = time.time()
    if isinstance(args[0], int) or isinstance(args[0], float):
        back = 0
    elif isinstance(args[0], list):
        back = list()
    else:
        back = ' '

    for elem in args:
        back += elem

    print('Сложение для {}, затрачено {} sec.'.format(type(args[0]), time.time() - start_time))
    print(back)


if __name__ == '__main__':
    args = [('aaa', 'bbbb', 'cccc'),
            (1, 2, 3, 4,),
            (1.1, 2.2, 3.3, 4.4,),
            ([1, 2, 3], ['asd', 'rrr'], [10.3, 2.2],)]

    def my_proc(func, args):
        multiprocess = []
        for arg in args:
            multiprocess.append(Process(target=func, args=arg))
        for p in multiprocess:
            p.start()
            yield p


    new_list = list(my_proc(add, args))

    for p in new_list:
        p.join()




