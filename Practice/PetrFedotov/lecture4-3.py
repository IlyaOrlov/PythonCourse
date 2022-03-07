def sorting(arr):
    for i in range(len(arr)):
        min_value = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_value]:
                min_value = j
        temp = arr[i]
        arr[i] = arr[min_value]
        arr[min_value] = temp

arr = [0, 3, 24, 2, 3, 7]
sorting(arr)
print(arr)