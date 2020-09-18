# 18.08.2020
# Реализовать итератор, который бы читал заданный текст по параграфам. Символ параграфа задается отдельно.

class MyIter():
    def __init__(self, text, symbol):
        self.text, self.symbol, self.partText = text, symbol, ""

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.partText = ""
        while self.i != len(self.text)-1:
            self.partText += self.text[self.i]
            self.i += 1

            if self.text[self.i] == self.symbol:
                self.i += 1
                return self.partText

            elif self.i == len(self.text)-1:
                self.partText += self.text[self.i]
                return self.partText

        else:
            raise StopIteration

iter = MyIter("The cat see a tree", " ")
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


