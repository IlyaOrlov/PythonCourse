from itertools import combinations_with_replacement
from itertools import chain
from itertools import filterfalse

def my_fun1(*args):
    for i in combinations_with_replacement(*args,len(*args)):
        yield i

s=my_fun1('password')
for i in s:
    print(i)
##############################################################
def my_fun2(*args):
    lst1=list(chain(*args))
    print(lst1)

lst=my_fun2([1,2,3], [4,5], [6,7])
##############################################################
def my_fun3(*args):
    data = list(filterfalse(lambda i: len(i) != 5, (*args)))
    print (data)

lst=my_fun3(['hello', 'i', 'write', 'cool', 'code'])