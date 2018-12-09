#for Python 3.6
#lecture 5 task 4

from itertools import chain, filterfalse, combinations


'''itertools.chain(*iterables) - возвращает по одному элементу
из первого итератора, потом из второго,
до тех пор, пока итераторы не кончатся.'''
print(list(chain([1,2,3], [4,5], [6,7])))

'''itertools.filterfalse(func, iterable) - все элементы,
для которых func возвращает ложь.'''
the_list = ['hello', 'i', 'write', 'cool', 'code']
print(list(filterfalse(lambda x: len(x) < 5, the_list)))

'''itertools.combinations(iterable, [r]) - комбинации длиной r
из iterable без повторяющихся элементов.'''
print(list(combinations('password', 4)))


