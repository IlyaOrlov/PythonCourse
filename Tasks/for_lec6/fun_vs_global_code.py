n = 4
for i in range(n):
    if i % 2 == 0:
        print(i)


def fun(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

f = fun(4)
# print(next(f))
# print(next(f))
# print(next(f))
for i in f:
    print(i)
