import time
from multiprocessing import Process

def find_primes(end,start):
    start_time = time.time()
    print('Поиск простых чисел от {} до {}'.format(start, end))
    res = []
    for elem in range(start, end):
        a = True
        for i in range(2, elem):
            if elem % i == 0:
                a = False
                break
        if a:
            res.append(elem)


    print('Результат поиска простых числе в диапазоне от {} до {}:'.format(start, end),res)
    print('Конец поиска простых чисел, затрачено {} sec.'.format(time.time() - start_time))


if __name__ == '__main__':
    args = [(10000, 3),
           (20000, 10001,),
           (30000, 20001,)]


    def my_proc(func, args):
        multiprocess = []
        for arg in args:
            multiprocess.append(Process(target=func, args=arg))
        for p in multiprocess:
            p.start()
            yield p


    new_list = list(my_proc(find_primes, args))

    for p in new_list:
        p.join()
        break