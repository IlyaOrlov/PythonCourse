def selection_sort(array):
    for i in range(len(array)):
        index_min_elem = array[i:].index(min(array[i:])) + i
        print(i, index_min_elem)
        array[i], array[index_min_elem] = array[index_min_elem], array[i]


# array = [4, 0, 5, 2, 5, 6, 9, 7]
array = [4, 0, 5, 4]
print(f"Before sorting {array}")
selection_sort(array)
print(f"After sorting {array}")
