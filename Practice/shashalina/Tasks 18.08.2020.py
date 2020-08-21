# 18.08.2020
# Реализовать итератор, который бы читал заданный текст по параграфам. Символ параграфа задается отдельно.

class MyIter():
    def __init__(self, text, symbol):
        self.text = text
        self.symbol = symbol
        self.parseText = text.split(self.symbol)

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i is not len(self.parseText):
            self.i+=1
            return self.parseText[self.i-1]
        else:
            raise StopIteration

iter = MyIter("THe cat see a tree", " ")
for x in iter:
   print(x)

# Написать генератор для построчного чтения файла.
import sys

def myGen(file):
    with open(file, "r+") as f:
        for i in f:
            yield i

for n in myGen("file.text"):
        sys.stdout.write(n)
