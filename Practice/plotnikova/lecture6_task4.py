# пример 1
import itertools


def fun(*iterables):
    print(list(itertools.chain(*iterables)))


fun([1,2], [3, 4], [5, 6, 7])


# пример 2
def fan2(x):
    print(list(itertools.filterfalse((lambda x: len(x) < 5 ), x)))


fan2(['hello','i','write', 'cool', 'code'])


# пример 3
def fan3(x):
    for item in itertools.combinations(x, 4):
        print(item)


fan3('password')