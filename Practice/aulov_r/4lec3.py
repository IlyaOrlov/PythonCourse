from random import randint
def choice(array):
    for i in range(len(array) - 1):
        m = i
        b = i + 1
        while b < len(array):
            if array[b] < array[m]:
                m = b
            b = b + 1
        array[i], array[m] = array[m], array[i]


arr = []
for i in range(6):
    arr.append(randint(1, 99))

print(arr)
choice(arr)
print(arr)


