# Реализовать итератор, который бы “читал” заданный текст по
# параграфам. Символ параграфа задается отдельно.


class Iter:
    def __init__(self, sym, st):
        self.st = st.split(sym)
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.st):
            ret = self.st[self.i]
            self.i += 1
            return ret
        else:
            raise StopIteration()


st = 'fgjfgjy\tjuiliedeh\tbdrtl.iop;\tcghkhk,ouil\thjk'

for i in Iter('\t', st):
    print(i)


# Написать генератор для построчного чтения файла.

def gen_fun():
    f = open('file.txt')
    for line in f:
        yield line
    f.close


line = gen_fun()
for i in line:
    print(i)
