def sorting(arr):
    for i in range(len(arr) - 1):
        min = i
        j = i + 1
        while j < len(arr):
            if arr[j] < arr[min]:
                min = j
            j = j + 1
        arr[i], arr[min] = arr[min], arr[i]
    print(arr)


arr = [0, -5, 34, 2, 3, -59]
sorting(arr)