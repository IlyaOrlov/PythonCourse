import itertools as it

first = ([1, 2, 3], [4, 5], [6, 7])
first_rep = list(it.chain.from_iterable(first))
print(first_rep)
second = ['hello', 'i', 'write', 'cool', 'code']
second_rep = list(it.filterfalse(lambda x: len(x) <= 4, second))
print (second_rep)
third = 'password'
third_rep = list(it.combinations(third, 4))
print(third_rep)