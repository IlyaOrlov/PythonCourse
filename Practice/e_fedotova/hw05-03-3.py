# лекция 4 задание 3

arr = [0,3,24,2,3,7]
N = len(arr)
i = 0
while i < N:
    m = i
    j = i + 1
    while j < N:
        if arr[j] < arr[m]:
            m = j
        j += 1
    arr[i], arr[m] = arr[m], arr[i]
    i += 1
print(arr)
