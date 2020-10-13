from itertools import chain
from itertools import filterfalse
from itertools import combinations


def itertools_usage(num: int, *args):
    count = 0                  # for check count of arrays

    for arg in args:
        if type(arg) is list:  # check type of arrays for choice of itertools methode
            count += 1

    if count == num:           # count of lists == num                     => use chain()
        return list(chain(*args))

    elif type(num) is int and len(args) == 1 and type(args[0]) is list:  # => use filterfalse()
        return list(filterfalse(lambda x: len(x) < num, args[0]))

    elif type(num) is int and len(args) == 1 and type(args[0]) is str:   # => use combinations()
        return list(combinations(args[0], num))

    return "Incorrect data!"


if __name__ == "__main__":
    print(itertools_usage(3, [5, 4], [3], [2, 1, 0]))
    print(itertools_usage(5, ["hello", "i", "write", "cook", "code", "embankment"]))
    print(itertools_usage(4, "password"))
    print(itertools_usage(4, 7, "incorrect data"))
    try:
        itertools_usage()
    except TypeError as ex:
        print(f"ERROR: {ex}")
