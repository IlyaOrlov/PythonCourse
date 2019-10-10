import time
from multiprocessing import Process

int_type = 1, 2, 3, 9, 8, 7
str_type = 'bfdQ', '123Q', '6jfgj6Q', 'dgkflk7'
lst_type = ['bfdQ', 5, 77, 'fgj'], [1, 2, '3Q'], [5, 6], ['468', 5, 'fgj']
type_list = int_type, str_type, lst_type

def addition(*args):
    new_str_type = ''
    new_int_type = 0
    new_lst_type = []
    if type(args[0]) is str:
        for i in args:
            new_str_type += i
        print(new_str_type)
    elif type(args[0]) is int:
        for i in args:
            new_int_type += i
        print(new_int_type)
    elif type(args[0]) is list:
        for i in args:
            new_lst_type += i
        print(new_lst_type)


if __name__ == '__main__':
    start = time.time()
    num_start = 1
    num_end = 0
    processes = []
    for j in type_list:
        num_start += 1
        num_end += 1
        #print(j)
        p = Process(target=addition, args=j)
        p.start()
        processes.append(p)

    for k in processes:
        k.join()

    print(f'время выполнения: {time.time() - start}')
