arr = [0, 3, 24, 2, 3, 7]


def sortirovka(array):
    i = 0
    while i < len(array):
        j = min(array[i:])
        m = array.index(j, i)
        if array[i] >= j:
            array[i], array[m] = array[m], array[i]
        else:
            continue
        i += 1


sortirovka(arr)
print(arr)


