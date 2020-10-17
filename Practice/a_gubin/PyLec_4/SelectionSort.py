def selection_sort(array):
    for index in range(len(array) - 1):
        index_min_elem = array.index(min(array[index:]))
        array[index], array[index_min_elem] = array[index_min_elem], array[index]


array = [4, 0, 5, 2, 5, 6, 9, 7]
print(f"Before sorting {array}")
selection_sort(array)
print(f"After sorting {array}")
