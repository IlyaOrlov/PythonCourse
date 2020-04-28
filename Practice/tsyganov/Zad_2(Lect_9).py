import multiprocessing
import time

def print_fun(*args):
    sum_str = ''
    sum_int = 0
    sum_list = 0
    i = 0
    for arg in args:
        if isinstance(arg, str):
            sum_str += arg
            i += 1
            if i == len(args):
                print(f'Сумма строк равна - {sum_str}')
        elif isinstance(arg, int):
            sum_int += arg
            i += 1
            if i == len(args):
                print(f'Сумма чисел равна - {sum_int}')
        elif isinstance(arg, list):
            for ar in arg:
                sum_list += ar
            print(f'Сумма списка равна - {sum_list}')

if __name__ == '__main__':
    t_1 = multiprocessing.Process(target = print_fun, args = ('Hello',' ','world',' ', '!'))
    t_2 = multiprocessing.Process(target = print_fun, args = ([1, 2, 3, 4],))
    t_3 = multiprocessing.Process(target = print_fun, args = (5, 11))

    list_t = [t_1, t_2, t_3]
    start = time.time()
    for t in list_t:
        t.start()
    for t in list_t:
            t.join()
    print(f'Время выполнения: {time.time()-start}')



