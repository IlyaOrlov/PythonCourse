import itertools as it
print(list(it.chain([1, 2, 3], [4, 5], [6, 7])))
print(list(it.filterfalse(lambda i: len(i) < 5,
           ['hello', 'i', 'write', 'cool', 'code'])))
print(list(it.combinations("password", 4)))
