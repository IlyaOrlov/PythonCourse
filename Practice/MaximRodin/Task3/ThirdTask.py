from random import randint


def sort(arr):
    for i in range(len(arr) - 1):
        b = i
        c = i + 1
        while c < len(arr):
            if arr[c] < arr[b]:
                b = c
            c = c + 1
        arr[i], arr[b] = arr[b], arr[i]


a = []
for i in range(10):
    a.append(randint(1, 99))

print(a)
sort(a)
print(a)