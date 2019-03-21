# Вариант 1
matrix = [[10, 2, 3, 5, 7],
        [3, 5, 99, 100, 21],
        [0, 8, 7, 4, 3],
        [1, 9, 3, 1, 2],
        [12, 11, 111, 661, 77]]
print(matrix)
z = int(input('Выберите и введите число из матрицы: '))


def kick_row(matrix, z):
    for i in matrix:
        for j in i:
            if z == j:
                n = i.index(z)
                for i in matrix:
                    del i[n]
                kick_row(matrix, z)
    return matrix


print(kick_row(matrix, z))

# Вариант 2
matrix = [[10, 2, 3, 5, 7],
        [3, 5, 99, 100, 21],
        [0, 8, 7, 4, 3],
        [1, 9, 3, 1, 2],
        [12, 11, 111, 661, 77]]
print(matrix)
z = int(input('Выберите и введите число из матрицы: '))


def kick_row(matrix, z):
    result = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    edited = [result[j] for j in range(len(result)) if z not in result[j]]
    finish = [[row[i] for row in edited] for i in range(len(edited[0]))]
    return finish
print(kick_row(matrix, z))



