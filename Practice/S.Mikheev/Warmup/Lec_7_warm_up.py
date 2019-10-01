st = "dvst\tdsvsdvvcascaac\tvacczvvsvvdvvxxvvsvsdv"


class My_Iterator:

    def __init__(self, text, it):
        self.text = text
        self.it = it
        self.num = self.text.find(self.it)

    def __iter__(self):
        return self

    def __next__(self):
        if self.num is None:
            raise StopIteration
        if self.num == -1:
            self.num = None
            return self.text
        elif self.num == 0:
            num = self.text.find(self.it, self.num + 1)
            if num == -1:
                text = self.text[self.num + 1:]
                self.num = None
                return text
            text = self.text[self.num + 1:num]
            self.text = self.text[num:]
            self.num = self.text.find(self.it)
            return text
        elif self.num > 0:
            text = self.text[:self.num]
            self.text = self.text[self.num:]
            self.num = self.text.find(self.it)
            return text


for i in My_Iterator(st, '\t'):
    print(i)
