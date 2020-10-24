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

class FunRanner:
    def __init__(self):
        self.fun_list = []
        self.__d = {}

    def add_fun(self, fun, *args):
        self.fun_list.append(fun)
        self.__d[fun] = args

    def remove_fun(self, fun):
        self.fun_list.remove(fun)
        del self.__d[fun]

    def run_all(self):
        for fun in self.__d.keys():
            fun(*self.__d.get(fun))

    def remove_all(self):
        self.fun_list = []
        self.__d.clear()

f = FunRanner()
f.add_fun(mysum, 1, 2)
f.add_fun(str_multyply, 'a', 5)
f.run_all()
f.remove_fun(mysum)
f.run_all()

