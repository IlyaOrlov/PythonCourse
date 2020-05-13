class FunRunner:
    def __init__(self):
        self.funs = []
    def add_fun(self, fun, *args, **kwargs):
        self.funs.append((fun, args, kwargs))
    def run_all(self):
        for i in self.funs:
            print(i)
        for f in self.funs:
            f[0](*f[1], **f[2])



def mysum(a, b):
    print(a + b)


def str_multiply(s, n=0):
    print(s*n)

f = FunRunner()
f.add_fun(mysum, 10, 20)   # {mysum: ((10, 20), {})}
f.add_fun(str_multiply, "a", n=5)  # {str_multiply: (("a", ), {'n': 5})}
f.run_all()