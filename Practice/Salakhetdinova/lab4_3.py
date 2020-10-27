import random

def sort(arr):
    for i in range(len(arr)):
        min_value = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_value]:
                min_value = j
 HEAD
                arr[i] = arr[min_value]
                arr[min_value] = arr[i]

        temp = arr[i]
        arr[i] = arr[min_value]
        arr[min_value] = temp

            
 c8db6ed0c1733acc791023d6cbb9cab97186a5ae

arr = []
for i in range(1, 7):
    arr.append(random.randint(1, 50))
print(arr)
sort(arr)
 HEAD
print(arr)

print(arr)
 c8db6ed0c1733acc791023d6cbb9cab97186a5ae
