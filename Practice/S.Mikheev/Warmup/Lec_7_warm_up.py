st = "\ndv\nstdsvsdvvcascaacv\nacczvvsvvdvvxxvvsvs\ndv"


class My_Iterator:

    def __init__(self, text, it):
        self.text = text
        self.it = it
        self.flag = True

    def __iter__(self):
        return self

    def __next__(self):
        if self.flag:
            num = self.text.find(self.it)
            text = self.text[:num].replace(self.it, "")
            if num == -1:
                num = 0
                text = self.text.replace(self.it, "")
                self.flag = False
            self.text = self.text[num:]
            return text
        else:
            raise StopIteration


for i in My_Iterator(st, '\t'):
    print(i)
