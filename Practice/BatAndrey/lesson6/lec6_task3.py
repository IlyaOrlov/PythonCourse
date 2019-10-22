import time as t


class MyContextManager:
    def __enter__(self):
        timer = t.process_time()
        print('time after code =', timer)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Code complite. Error info:type - {}'.format(exc_type))


with MyContextManager():
    a = max([1, 2, 3, 4, 5, 6, 32423, 532523, 253, 2332, 232342, 765756, 56858565])
    b = sum([1232132131, 143333334, 12323])
