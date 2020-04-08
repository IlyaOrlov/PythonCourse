from random import randint

arr = [randint(0, 100) for i in range(6)]



def sortirovka(array):
    i = 0
    while i < len(array):
        j = min(array[i:])
        m = array.index(j, i)
        if array[i] >= j:
            array[i], array[m] = array[m], array[i]
        i += 1


print(arr)
sortirovka(arr)
print(arr)
