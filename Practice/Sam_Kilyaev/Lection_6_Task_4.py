import itertools


def options(psswd, long):
    result = itertools.combinations(psswd, long)
    output = []
    for i in result:
        output.append(next(result))
    return output


psswd = 'password'
long = 4
print(options(psswd, long))


def three_massiv_to_one(*args):
    my_list = list(itertools.chain(*args))
    return my_list


print(three_massiv_to_one([1, 2, 3], [5, 7, 6], [8, 9, 0]))


def massiv_5(massiv):
    my_list = list(itertools.filterfalse(lambda i: len(i) < 5, massiv))
    return my_list


print(massiv_5(['hello', 'one', 'write']))
