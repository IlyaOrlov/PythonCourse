from itertools import chain
from itertools import filterfalse
from itertools import combinations

def funcChain (a, b , c): 
    print (list(chain(a, b, c)))
funcChain ([1, 2, 3], [4, 5, 6], [7, 8, 9] )


def funcFiltr(data):
    print (list(filterfalse(lambda i: len(i) < 5 , data)))
funcFiltr(['hello', 'i', 'write', 'cool', 'code'])


def funcCombin(string):
    print (list(combinations(string, 4)))
funcCombin('password')
