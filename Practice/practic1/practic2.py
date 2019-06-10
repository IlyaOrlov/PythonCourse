# from itertools import chain
from itertools import *


def func1(a=[], b=[], c=[]):
    my_list = list(chain(a, b, c))
    return my_list


print(func1([1, 2, 3], [4, 5], [6, 7]))


def func2(a=[]):
    my_list = list(filterfalse(lambda x: len(x) != 5, a))
    return my_list


print(func2(['hello', 'i', 'write', 'cool', 'code']))


def func3():
    string = "password"
    my_list = list(combinations(string, 4))
    return my_list


print(func3())
