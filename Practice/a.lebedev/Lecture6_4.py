import itertools as qwe

first = ([1, 2, 3], [4, 5], [6, 7])
first_rep = list(qwe.chain.from_iterable(first))
print(first_rep)
second = (['hello', 'i', 'write', 'cool', 'code'])
second_rep = list(qwe.filterfalse(lambda x: len(x) <= 4, second))
print (second_rep)
third = 'password'
third_rep = list(qwe.combinations(third, 4))
print(third_rep)