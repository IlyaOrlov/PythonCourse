import itertools


def joinedlist(*lists):
    return itertools.chain(*lists)


print([i for i in joinedlist([1, 2, 3], [4, 5], [6, 7])])