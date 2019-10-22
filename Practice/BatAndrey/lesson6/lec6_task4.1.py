from itertools import chain

def join_array(*args):
    add_array = list(chain(*args))
    print(add_array)


join_array([1, 2, 3], [4, 5], [6, 7])