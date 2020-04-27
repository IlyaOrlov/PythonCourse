from itertools import chain,combinations,filterfalse

lst1 = [1, 2, 3]
lst2 = [4, 5]
lst3 = [6, 7]

my_list = list(chain(lst1, lst2, lst3))
print(my_list)

lst = ['hello', 'i', 'write', 'cool', 'code']
data = list(filterfalse(lambda x: len(x) !=5, lst))
print(data)


ln= 'password'
data = list(combinations(ln, 4))
print(data)



