# without Python methods
arr = [0, 3, 24, 2, 3, 7]
minimum = arr[0]
minimum_index = 0
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[j] < minimum:
            minimum = arr[j]
            minimum_index = j
    arr[i], arr[minimum_index] = arr[minimum_index], arr[i]
    minimum = arr[i + 1]
print(arr)

# with Python methods
arr = [0, 3, 24, 2, 3, 7]
for i in range(len(arr)-1):
    minimum_index = arr.index(min(arr[i:]), i)
    arr[i], arr[minimum_index] = arr[minimum_index], arr[i]
print(arr)
