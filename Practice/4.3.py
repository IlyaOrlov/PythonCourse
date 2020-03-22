arr = [0, 3, 24, 2, 3, 7]

for i in range(len(arr)):
    x = min(arr[i:])
    j = arr[i:].index(x) + i
    arr.insert(i, arr.pop(j))
print(arr)
