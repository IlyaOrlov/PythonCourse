import time
from multiprocessing import Process


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
    args = [('aaa', 'bbbb', 'cccc', 'dddd',),
            (1, 2, 3, 4,),
            (5.5, 7.8, 3.4, 5.6,),
            ([1, 2, 3, 4, 5], [10, 55, 77, 89], ['asd', 'rrr'], [12.3, 13.2],)]


    # processes = []
    # for arg in args:
    #     processes.append(Process(target=adder, args=arg))
    # for p in processes:
    #     p.start()
    # for p in processes:
    #     p.join()


    def my_gen_proc(func, args):  # Функция-генератор процессов
        processes = []
        for arg in args:
            processes.append(Process(target=func, args=arg))
        for p in processes:
            p.start()
            yield p


    plist = list(my_gen_proc(adder, args))  # список всех запущенных процессов

    for p in plist:
        p.join()

    # for p in my_gen_proc(adder, args):
    #     p.join()
