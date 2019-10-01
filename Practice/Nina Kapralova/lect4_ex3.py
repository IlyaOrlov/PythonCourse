arr = [0, 3, 24, 2, 3, 7]
i = len(arr)
for n in range(i):
    a = min(arr[n:])
    b = arr.index(a, n)
    arr[n], arr[b] = arr[b], arr[n]
print(arr)