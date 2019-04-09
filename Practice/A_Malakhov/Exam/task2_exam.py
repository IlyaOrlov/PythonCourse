class Iteration:
    lst = []
    def __init__(self, n):
        self.n = n
        self.k = 1


    def __iter__(self):
        return self

    def __next__(self):
        a = 2
        while self.k < self.n + 1:
            is_prime = False
            for i in self.lst:
                if a % i == 0:
                    is_prime = True
                    break
            if is_prime == False:
                self.k += 1
                self.lst.append(a)
                yield a
            a += 1


try:
    for i in Iteration(20):
        print(next(i), end=' ')
except StopIteration:
    print('')
