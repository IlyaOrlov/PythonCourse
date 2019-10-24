import time
from multiprocessing import Process

int_type = 1, 2, 3, 9, 8, 7
str_type = 'bfdQ', '123Q', '6jfgj6Q', 'dgkflk7'
lst_type = ['bfdQ', 5, 77, 'fgj'], [1, 2, '3Q'], [5, 6], ['468', 5, 'fgj']
type_list = int_type, str_type, lst_type

def addition(*args):
    if type(args[0]) is str:
        new_type = ''
    elif type(args[0]) is int:
        new_type = 0
    elif type(args[0]) is list:
        new_type = []
    for i in args:
        new_type += i
    print(new_type)


if __name__ == '__main__':
    start = time.time()
    processes = []
    for j in type_list:
        p = Process(target=addition, args=j)
        p.start()
        processes.append(p)

    for k in processes:
        k.join()

    print(f'время выполнения: {time.time() - start}')
