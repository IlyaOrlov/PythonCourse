import itertools


def mycombination(x, mystr):
    return itertools.combinations(mystr, x)


for i in mycombination(4, 'password'):
    print(i)

# print([i for i in mycombination(4, 'password')])
