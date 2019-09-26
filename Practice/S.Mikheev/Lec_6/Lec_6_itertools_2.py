import itertools


def myfiltr(x, lists):
    return itertools.filterfalse(lambda elem: len(elem) < x, lists)


print([i for i in myfiltr(5, ['hello', 'i', 'write', 'cool', 'code'])])