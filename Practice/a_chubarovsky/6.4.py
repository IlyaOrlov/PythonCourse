import itertools as it

arr1 = [1, 2, 3]
arr2 = [4, 5]
arr3 = [6, 7]
arr4 = ['hello', 'i', 'write', 'cool', 'code']
str1 = 'password'

arr5 = list(it.chain(arr1, arr2, arr3))
print(arr5)
arr6 = list(it.filterfalse(lambda x: len(x) != 5, arr4))
print(arr6)
data = list(it.combinations(str1, 4))
for element in data:
    print(element)
