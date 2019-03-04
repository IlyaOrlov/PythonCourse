# лекция 4 задание 3

arr = [0,3,24,2,3,7]
i = 0
while i < len(arr):
    m = i
    j = i + 1
    while j < len(arr):
        if arr[j] < arr[m]:
            m = j
        j += 1
    arr[i], arr[m] = arr[m], arr[i]
    i += 1
print(arr)
