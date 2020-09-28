import random

def sort(arr):
    for i in range(len(arr)):
        min_value = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_value]:
                min_value = j
                arr[i] = arr[min_value]
                arr[min_value] = arr[i]

arr = []
for i in range(1, 7):
    arr.append(random.randint(1, 50))
print(arr)
sort(arr)
print(arr)