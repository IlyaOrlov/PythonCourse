st = "dvsdsvsdvv\tcascaacvac\tczvvsvvdv\tvxxvvsvsdv"


class My_Iterator:

    def __init__(self, text, it):
        self.text = text
        self.it = it
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        a = self.text.split(self.it)
        if self.num < len(a):
            word = a[self.num]
            self.num += 1
            return word
        else:
            raise StopIteration


for i in My_Iterator(st, '\t'):
    print(i)
