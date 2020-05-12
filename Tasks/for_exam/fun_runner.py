class FunRunner:
    def __init__(self):
        self.funs = {}
    def add_fun(self, fun, *args, **kwargs):
        self.funs[fun] = [args, kwargs]
    def del_fun(self, fun):
        del self.funs[fun]
    def run_all(self):
        for f, ar in self.funs.items():
            f(*ar[0], **ar[1])


def mysum(a, b):
    print(a + b)


def str_multiply(s, n=0):
    print(s*n)

f = FunRunner()
f.add_fun(mysum, 10, 20)
f.add_fun(str_multiply, "a", n=5)
f.run_all()


