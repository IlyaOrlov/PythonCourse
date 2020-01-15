arr = [0, 3, 24, 2, 3, 7]
i = 0

while i < len(arr):
    indmin = arr.index(min(arr[i:]), i)
    arr[indmin], arr[i] = arr[i], arr[indmin]
    i += 1

print(arr)