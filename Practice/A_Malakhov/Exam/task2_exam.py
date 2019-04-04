class Iteration:
    lst = []

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        a = 2
        k = 1
        while k < self.n + 1:
            counter = 0
            for i in self.lst:
                if a % i == 0:
                    counter += 1
            if counter == 0:
                self.lst.append(a)
                yield a
                k += 1
            else:
                counter = 0
            a += 1
            if k == self.n + 1:
                break


for i in Iteration(20):
    print(i, end=' ')
