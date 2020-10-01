import random


def choise_sort(arr):
    for i in range(len(arr)):
        min_value = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_value]:
                min_value = j
        arr[i], arr[min_value] = arr[min_value], arr[i]


arr = []
for i in range(1, 26):
    arr.append(random.randint(1, 100))
choise_sort(arr)
print(arr)
