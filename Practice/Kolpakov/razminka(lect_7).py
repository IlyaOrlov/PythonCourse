# Реализовать итератор, который бы “читал” заданный текст по
# параграфам. Символ параграфа задается отдельно.


class Iter:
    def __init__(self, sym, st):
        self.st = st
        self.sym = sym
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.st):
            lst = []
            while self.i < len(self.st):
                if self.st[self.i] != self.sym:
                    lst.append(self.st[self.i])
                else:
                    self.i += 1
                    break
                self.i += 1
            return ''.join(lst)


        else:
            raise StopIteration


st = 'fgjfgjy\tjuiliedeh\tbdrtl.iop;\tcghkhk,ouil\thjk'

for i in Iter('\t', st):
    print(i)
print('---------------')

# Написать генератор для построчного чтения файла.

def gen_fun():
    f = open('file.txt')
    for line in f:
        yield line
    f.close


line = gen_fun()
for i in line:
    print(i)
