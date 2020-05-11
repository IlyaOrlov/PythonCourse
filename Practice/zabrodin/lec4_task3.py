from random import randint

arr = [randint(0, 100) for i in range(6)]


def sortirovka(array):
    i = 0
    while i < len(array):
        j = min(array[i:])
        m = array.index(j, i)
        array[i], array[m] = array[m], array[i]
        i += 1
    return array


print(arr)
p = sortirovka(arr)
print(p)
