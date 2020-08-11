def selection_sort(*args):
    array = list(args)

    for i in array:
        min_num = i
        index = -1
        index_min = 0

        for j in array:  # for every i
            index += 1
            if j < min_num and index > array.index(i):
                min_num = j
                index_min = index

        if min_num != i:
            array[array.index(i)], array[index_min] = min_num, i

    print(array)


selection_sort(5, 3, 6, 9, 3, 44, -9)    # for testing
