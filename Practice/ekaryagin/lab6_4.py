import itertools


def iter_1(list_1, list_2, list_3):
    return list(itertools.chain(list_1, list_2, list_3))


def iter_2(lst):
    return list(itertools.filterfalse(lambda i: len(i) < 5, lst))


def iter_3(lst, length):
    return list(itertools.combinations(lst, length))


print(iter_1([1, 2, 3], [4, 5], [6, 7]))
print(iter_2(['hello', 'i', 'write', 'cool', 'code']))
print(iter_3('password', 4))
