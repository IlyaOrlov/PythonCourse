class MyIterator:
    def __init__(self, txt, sym):
        self.txt = txt
        self.sym = sym
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < len(self.txt):
            lst = []
            while self.i < len(self.txt) and self.txt[self.i] != self.sym:
                lst.append(self.txt[self.i])
                self.i += 1
            self.i += 1
            return ''.join(lst)
        else:
            raise StopIteration


def MyGenerator(txt, sym):
    i = 0
    while i < len(txt):
        lst = []
        while i < len(txt) and txt[i] != sym:
            lst.append(txt[i])
            i += 1
        i += 1
        yield ''.join(lst)

txt = "This is a table\tLondon is capital of Great Britain\tSomething else"

it = MyIterator(txt, "\t")
for i in it:
    print(i)
# "This is a table"
# "London is capital of Great Britain"
# "Something else"

gen = MyGenerator(txt, "\t")
for i in gen:
    print(i)
# "This is a table"
# "London is capital of Great Britain"
# "Something else"

