#arr = [0, 3, 24, 2, 3, 7]
#arr.sort()
#print(arr)

arr = [0, 3, 24, 2, 3, 7]


def select_sort(arr):
    i = 0
    while i < len(arr) - 1:
        a = i
        j = i + 1
        while j < len(arr):
            if arr[j] < arr[a]:
                a = j
            j += 1
#такую замену элементов списка честно загуглил,
#через 3-ю переменную никак не выходит результат
        arr[i], arr[a] = arr[a], arr[i]
        i += 1
    print(arr)


select_sort(arr)