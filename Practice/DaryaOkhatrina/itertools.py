import itertools as it


def fun(lst, lst1, lst2):
    end_lst = list(it.chain(lst, lst1, lst2))
    return end_lst

print(fun([1, 2, 3], [4, 5], [6, 7]))


s = 'password'
def fun2(s):
    s1 = list(it.combinations(s, 4))
    return s1

print(fun2(s))

s2 = ['hello', 'i', 'write', 'cool', 'code']

def fun3(s2):

    s3 = list(it.filterfalse(lambda x: len(x)!= 5, s2))
    return s3

print(fun3(s2))

