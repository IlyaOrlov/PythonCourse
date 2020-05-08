import itertools


def chain(lst1, lst2, lst3):
    joint = list(itertools.chain(lst1, lst2, lst3))
    return joint


def filtrate(lst):
    filtered = list(itertools.filterfalse(lambda x: len(x) < 5, lst))
    return filtered


def combination(string, r):
    passwords = list(itertools.combinations(string, r))
    return passwords


print(chain([1, 2, 3], [4, 5], [6, 7]))
print(filtrate(['hello', 'i', 'write', 'cool', 'code']))
print(combination('password', 4))
