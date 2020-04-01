import random


n, m = [int(i) for i in input('Введите через пробел размер матрицы: ').split(' ')]
matrix = [[random.randint(0, 9) for j in range(m)] for i in range(n)]
for row in matrix:
    print(row)
number = int(input('Столбец с какой цифрой удалить: '))

def transp(matrix):
    transp_matrix = []
    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        transp_matrix.append(row)
    return transp_matrix

def del_row(matrix, number):
    lst = [i for i in range(len(matrix))]
    lst.reverse()
    for i in lst:
        if number in matrix[i]:
            del matrix[i]
    return matrix

matrix = transp(matrix)
matrix = del_row(matrix, number)
matrix = transp(matrix)

for row in matrix:
    print(row)
