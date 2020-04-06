a = [
    [2, 5, 7, 3, 5],
    [3, 11, 43, 2, 9],
    [5, 8, 32, 13, 6],
    [4, 2, 1, 4, 8]
]
number = input('Введите число :')

for i in reversed(range(len(a))):
    for j in reversed(range(len(a[i]))):
        if a[i][j] == int(number):
            for n in a:
                n.pop(j)

print(a)



