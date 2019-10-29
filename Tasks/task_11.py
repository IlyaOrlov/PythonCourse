import time

class Scheduler:
    def __init__(self, worktime=None):
        self._fun_list = []
        self._worktime = worktime

    def add_fun(self, fun, period, *args, **kwargs):
        self._fun_list.append({'fun':fun, 'period':period, 'last':0,
                               'args':args, 'kwargs':kwargs})

    def run(self):
        start_time = time.perf_counter()
        while (self._worktime is None) or (time.perf_counter() - start_time < self._worktime):
            for each in self._fun_list:
                t = time.perf_counter()
                if each['last'] == 0 or t - each['last'] > each['period']:
                    each['last'] = t
                    res = each['fun'](*each['args'], **each['kwargs'])
                    print('Time {}, fun {}, result: {}'.format(t, each['fun'].__name__, res))

def mysum(a,b):
    return a+b

def mydif(a,b):
    return a-b

def sayhello():
    return 'hello'

def nothing():
    pass


if __name__ == '__main__':
    s = Scheduler()
    s.add_fun(mysum, 5, 10, 20)
    s.add_fun(mydif, 5, 10, 20)
    s.add_fun(sayhello, 10)
    s.add_fun(nothing, 10)
    s.run()
