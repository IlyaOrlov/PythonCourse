#1
def fun(lst):
    sep = '*'
    d = {x: lst.count(x) for x in set(lst)}
    temp = sorted([str(d.get(x))+sep+str(x) for x in d.keys()])
    res = [int(x.split(sep)[1]) for x in temp]
    return res

print(fun([8,8,1,2,3,3,3,4,5,5,6]))

#3
def mysum(a,b):
    print(a+b)

def str_multyply(s, n=0):
    print(s*n)

def print_multydict(*args, **kwargs):
    for key, value in kwargs.items():
        for arg in args:
            print('key = {} , value * arg = {}'.format(key, value * arg))


class FunRanner:
    def __init__(self):
        self.fun_list = []
        self.__args = {}
        self.__kwargs = {}

    def add_fun(self, fun, *args, **kwargs):
        self.fun_list.append(fun)
        self.__args[fun] = args
        self.__kwargs[fun] = kwargs

    def remove_fun(self, fun):
        self.fun_list.remove(fun)
        del self.__args[fun]
        del self.__kwargs[fun]

    def run_all(self):
        for fun in self.fun_list:
            fun(*self.__args.get(fun), **self.__kwargs.get(fun))

    def remove_all(self):
        self.fun_list = []
        self.__args.clear()
        self.__kwargs.clear()

f = FunRanner()
f.add_fun(mysum, 1, 2)
f.add_fun(str_multyply, 'a', 5)
f.add_fun(print_multydict, 3, 5, a=1, b=5)
f.run_all()
f.remove_fun(mysum)
f.run_all()

