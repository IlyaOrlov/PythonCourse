# Реализовать алгоритм сортировки выбором

arr = [1, 4, 6, 3, 6 - 1, 0, -12, 55, -143]


def Sort(arr):
    N = len(arr)
    for i in range(N - 1):
        for j in range(i + 1, N):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


print(Sort(arr))
