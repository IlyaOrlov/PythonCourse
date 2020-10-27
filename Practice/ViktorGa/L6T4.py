from itertools import chain
from itertools import filterfalse
from itertools import combinations


def merge_array(arr):
    result = list(chain.from_iterable(arr))
    return result

def filter_array(arr):
    result = list(filterfalse(lambda x: len(x)<5,arr))
    return result

def combinate_text(text):
    result =list(combinations(text,len(text)-4))
    return result


a = ([1,2,3],[4,5],[6,7])
print(merge_array(a))

a = ['hello','i','write','cool','code']
print(filter_array(a))

a = 'password'
print(combinate_text(a))