import itertools


def arr(num1, num2, num3):
    joint = list(itertools.chain(num1, num2, num3))
    return joint

def less(lst):
    filtered = list(itertools.filterfalse(lambda x: len(x) != 5, lst))
    return filtered

def key(string, r):
    passwords = list(itertools.combinations(string, r))
    return passwords

print(arr([1, 2, 3], [4, 5], [6, 7]))
print(less(['hello', 'i', 'write', 'cool', 'code']))
print(key('password', 4))