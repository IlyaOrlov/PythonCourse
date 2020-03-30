import random as rdm


def del_column(arr, index):
    for row in arr:
        row.pop(index)
    return arr


x = 5
y = 5

array = [[0] * x for i in range(y)]
for i in range(y):
    for j in range(x):
        array[i][j] = rdm.randint(0, 20)
for i in array:
    print('{}'.format(i), end='')
    print()
elem_to_del = int(input("Input an element to delete: "))
k = 0
for i in range(y):
    for j in range(x):
        if array[i][j-k] == elem_to_del:
            column_to_del = [array[i][j-k], j-k]
            del_column(array, column_to_del[1])
            k += 1


for i in array:
    print('{}'.format(i), end='')
    print()
