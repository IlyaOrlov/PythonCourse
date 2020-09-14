import itertools


def sum_chain(arr):
    return list(itertools.chain.from_iterable(arr))


def pass_comb(data):
    global lst
    for result in itertools.combinations(data, 4):
        lst.append(result)
    return lst


def filter_false(data):
    return list(itertools.filterfalse(lambda x: len(x) < 5, data))




if __name__ == "__main__":

    value = ([1, 2, 3], [4, 5], [6, 7])
    print(sum_chain(value))
    st = 'password'
    lst = []
    print(pass_comb(st))
    text = ['hello', 'i', 'write', 'cool', 'code']
    print(filter_false(text))

