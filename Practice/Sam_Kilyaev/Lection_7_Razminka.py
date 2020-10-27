def reader(file):
    with open(file, 'r') as my_file:
        for i in my_file.readlines():
            yield i


l = reader('test.txt')
print(next(l))
print(next(l))


# § - символ параграфа

class IterParagraf:
    def __init__(self, text, symbol):
        self.text = text
        self.symbol = symbol

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.results = ""
        while self.i != len(self.text) - 1:
            self.results += self.text[self.i]
            self.i += 1
            if self.text[self.i] == self.symbol:
                self.i += 1
                return self.results
            elif self.i == len(self.text) - 1:
                self.results += self.text[self.i]
                return self.results
        else:
            raise StopIteration


MyIterator = IterParagraf("We§can§do§it§this", "§")
for x in MyIterator:
   print(x)