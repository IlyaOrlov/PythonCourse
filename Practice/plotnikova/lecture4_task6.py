# транспонирование матрицы
def transpose_matrix(a):
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


# Удаление столбцов
def delete_column(a, b):
    for row in a:
        try:
            row.index(b)
        except ValueError:
            pass
        else:
            a.pop(a.index(row))
    return a


# Пример матрицы
matrix = [[1, 2, 3, 8, 3],
          [4, 5, 6, 9, 4],
          [4, 5, 6, 11, 3],
          [4, 5, 6, 35, 5],
          [4, 5, 6, 44, 2]]

# Число для удаления столбца
b = 5
#ответ:
print(transpose_matrix(delete_column(transpose_matrix(matrix), b)))