import itertools


def multiplier(m=1, source=[1, 2, 3]):
    result = source
    for i in range(len(source)):
        result[i] *= m
    return result
print(multiplier(5))
print(multiplier(12, [1, 2]))


def chargen():
    for c in '0123456789':
        yield int(c)
words = [c+c for c in chargen()]
print(words)


print(list(itertools.combinations('password', 4)))

print(list(itertools.chain([1, 2, 3], [4, 5], [6, 7])))

lst = sorted(('hello', 'i', 'write', 'cool', 'code'), key=len, reverse=True)
print(lst)
print(list(itertools.takewhile(lambda x: len(x) > 4, lst)))