""" Реализовать алгоритм сортировки выбором. Алгоритм состоит из следующих шагов:
1. найти наименьший элемент в массиве !
2. поменять местами его и первый элемент в массиве
3. найти следующий наименьший элемент в массиве
4. и поменять местами его и второй элемент массива
5. продолжать это пока весь массив не будет отсортирован
arr = [0,3,24,2,3,7]
"""

arr = [1, 3, 24, 2, 3, 0, 2, 4, 100, 50, -2, -45]


def selection_sort(array):
    for i in range(len(array)):  # 0 1 2 3 4 5
        min_index = i

        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]


print(arr)
selection_sort(arr)
print(arr)
