# Сложность алгоритма сортировки слиянием O(nlog (n))
# Сложность доступа к элементам отсортированного листа O(n)
# Сложность алгоритма выбора O(nlog (n)) + O(n), что можно сократить до O(nlog (n))


def max_numbers(arr, n):
    reverse_sorted_arr = reverse_sort_numbers(arr)
    max_numbers_arr = []
    for i in range(n):
        max_numbers_arr.append(reverse_sorted_arr[i])
    return max_numbers_arr


def reverse_sort_numbers(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_list = reverse_sort_numbers(arr[:mid])
    right_list = reverse_sort_numbers(arr[mid:])
    return merge(left_list, right_list)


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)
    for i in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] >= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list


array = [1, 6, 2, 15, 12, 3, 45, 24]
print(max_numbers(array, 3))
