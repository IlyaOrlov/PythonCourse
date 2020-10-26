# -*- coding: utf8 -*-
# Реализовать запуск функции, осуществляющей операцию сложения для различных типов (integer, string, list)
# параллельно с различными наборами аргументов

from multiprocessing import Process

def sum(*args):
    res_int = 0
    res_str = ''
    res_lst = []
    for arg in range(len(args)):
        if isinstance(args[arg], int):
            res_int += args[arg]
        elif isinstance(args[arg], str):
            res_str += args[arg]
        elif isinstance(args[arg], list):
            res_lst += args[arg]

lst_values = [[['a'], [1], ['b']], [2, 3, 4, 5], ['c', 'd', 'e', 'f']]
prcs = []

if __name__ == '__main__':
    for values in lst_values:
        prc = Process(target=sum, args=values)
        prc.start()
        prcs.append(prc)

    for prc in prcs:
        prc.join()
