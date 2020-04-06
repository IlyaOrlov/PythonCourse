import random as rdm


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
for i, e in reversed(list(enumerate(array))):
    for j, f in reversed(list(enumerate(e))):
        if array[i][j] == elem_to_del:
            for row in array:
                row.pop(j)


for i in array:
    print('{}'.format(i), end='')
    print()
