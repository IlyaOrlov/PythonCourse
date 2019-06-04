import random


def del_column(matrix, key, n, m):
    k = g = 0
    while k < n:
        while g < m:
            if matrix[k][g] == key:
                if g == m - 1:
                    m = m - 1
                    a = 0
                    while a < n:
                        matrix[a] = matrix[a][0: g:]
                        a += 1
                else:
                    m = m - 1
                    a = 0
                    while a < n:
                        temp = matrix[a][g + 1::]
                        matrix[a] = matrix[a][0: g:]
                        matrix[a].extend(temp)
                        a += 1
            g += 1
        k += 1
        g = 0
    return matrix


i = j = 0
N = M = 5
# генерируем матрицу из нулей:
mat = [[0 for i in range(0, N)] for j in range(0, M)]
# заполняем матрицу случайными числами в диапазоне от 0 до 9:
while i < N:
    while j < M:
        mat[i][j] = random.randint(0, 9)
        j += 1
    print(mat[i])
    j = 0
    i += 1
print('\n')

i = 0
mat = del_column(mat, 0, N, M)
while i < N:
    print(mat[i])
    i += 1
