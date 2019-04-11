class Iteration:
    def __init__(self, n):
        self.n = n
        self.lst = []
        self.k = 0
        self.a = 2

    def __iter__(self):
        return self

    def __next__(self):
        while self.k < self.n:
            is_prime = False
            for i in self.lst:
                if self.a % i == 0:
                    is_prime = True
                    break
            if is_prime == False:
                self.k += 1
                self.lst.append(self.a)
                return self.a
            self.a += 1
        else:
            raise StopIteration


for i in Iteration(20):
    print(i, end=' ')
