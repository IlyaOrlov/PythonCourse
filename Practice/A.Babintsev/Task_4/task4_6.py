"""
Есть список списков (матрица). Каждый внутренний список - это строка матрицы.
Необходимо реализовать функцию, которая удаляет столбец, который содержит заданную
цифру
"""


matrix1 = [[1, 2, 3, 3], [8, 8, 6, 8], [7, 8, 8, 3], [7, 8, 9, 3]]
print(matrix1)
x = 8  # будем удалять по этому значению
y = None
r = len(matrix1[0])
for rr in range(r):
    y = None
    i = len(matrix1)
    j = len(matrix1[0])
    for ii in range(i):
        for jj in range(j):
            if x == matrix1[ii][jj]:
                y = jj
                break
    for ii in range(i):
        del matrix1[ii][y]
    print(matrix1)
