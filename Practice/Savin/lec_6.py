import itertools


def multiplier(m=1, source=None):
    if source == None:
        source = [1, 2, 3]
    for i in range(len(source)):
        source[i] *= m
    return source
print(multiplier(5))
print(multiplier(5))
print(multiplier(12, [1, 2]))


def chargen():
    for c in '0123456789':
        yield int(c)
words = [c+c for c in chargen()]
print(words)


print(list(itertools.combinations('password', 4)))

print(list(itertools.chain([1, 2, 3], [4, 5], [6, 7])))

print(list(itertools.filterfalse(lambda x: len(x) < 5, ('hello', 'i', 'write', 'cool', 'code'))))