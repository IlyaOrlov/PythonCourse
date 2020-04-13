class MyIterClass:
    def __init__(self, n):
        self.num = n
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < self.num:
            res = self.i
            self.i += 2
            return res
        else:
            raise StopIteration


m = MyIterClass(50)
# it_m = iter(m)
# print(next(it_m))  # n.__next__
# print(next(it_m))
# print(next(it_m))
# print(next(it_m))
for i in m:
    print(i)