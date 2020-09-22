import itertools

def onearr(lst1, lst2, lst3):
    arr = list(itertools.chain(lst1, lst2, lst3))
    return arr

def filtarr(lst):
    filter = list(itertools.filterfalse(lambda x: len(x) < 5, lst))
    return filter

def combination(string, r):
    password = list(itertools.combinations(string, r))
    return password

print(onearr([1, 2, 3], [4, 5], [6, 7]))
print(filtarr(['hello', 'i', 'write', 'cool', 'code']))
print(combination('password', 4))