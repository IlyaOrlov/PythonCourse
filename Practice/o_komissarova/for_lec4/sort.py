# Реализовать алгоритм сортировки выбором.

def sort(array):
    for i in range(0, len(array) - 1):
        pos_for_change = i
        minimum = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minimum]:
                minimum = j
        array[pos_for_change], array[minimum] = array[minimum], array[pos_for_change]


arr = [0, 3, 24, 2, 3, 7]
print(arr)
sort(arr)
print(arr)

