import itertools

print(list(itertools.chain([1, 2, 3], [4, 5], [6, 7])))
print(list(itertools.filterfalse(lambda x: len(x) < 5, ['hello', 'i', 'write', 'cool', 'code'])))
print(list(itertools.combinations('password', 4)))
