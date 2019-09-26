# пример 1
import itertools


def fun(*iterables):
    print(list(itertools.chain(*iterables)))


fun([1,2], [3, 4], [5, 6, 7])


# пример 2
def fan1(x):
    return len(x) < 5 and True or False


def fan2(x):
    print(list(itertools.filterfalse(fan1, x)))

fan2(['hello','i','write', 'cool', 'code'])


# пример 3
def fan3(x):
    for item in itertools.combinations(x, 4):
        print(item)


fan3('password')