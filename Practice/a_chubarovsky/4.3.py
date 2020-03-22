arr = [0, 3, 24, 2, 3, 7]


def sort(array):
    for i in range(1, len(array)):
        swapped_element = array[i]
        j = i - 1
        while j >= 0 and array[j] > swapped_element:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = swapped_element


sort(arr)
print(arr)
