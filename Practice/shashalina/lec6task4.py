from itertools import chain
from itertools import filterfalse
from itertools import permutations

# Функция должна принимать три массива ([1, 2, 3], [4, 5], [6, 7]), а вернуть лишь один массив ([1, 2, 3, 4, 5, 6, 7])

def myUnification(*args):
     newArr = list(chain(*args))
     print(newArr)

myUnification([1, 2, 3], [4, 5], [6, 7])

# Функция принимает массив (['hello', 'i', 'write', 'cool', 'code']) и возвращает массив из элементов,
# у которых длина не меньше пяти (['hello', 'write'])

def myCheckLength(arr):
     filteredArr = list(filterfalse(lambda i: len(i) < 5 , arr))
     print(filteredArr)

myCheckLength(['hello', 'i', 'write', 'cool', 'code'])

#  Функция выдает на строку 'password' все возможные комбинации вида
# ([('p', 'a', 's', 's'), ('p', 'a', 's', 'w'), ('p', 'a', 's', 'o'), ...)

def myCombination(word):
    arr = []
    for i in permutations(word, 4):
        arr.append(i)
    print(arr)

myCombination('password')
