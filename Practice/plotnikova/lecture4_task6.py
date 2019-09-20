# транспонирование матрицы
def transpose_matrix(a):
    if len(a)!=0:
        return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
    else:
        return a


# Удаление столбцов
def delete_column(a, b):
    for row in a:
        if b in row:
            a.remove(row)
    return a


# Пример матрицы
matrix = [[1, 2, 3, 8, 3],
          [4, 5, 6, 9, 4],
          [4, 5, 6, 11, 3],
          [4, 5, 6, 35, 5],
          [4, 5, 6, 44, 2]]

#matrix=[]

# Число для удаления столбца
b =5
#ответ:
print(transpose_matrix(delete_column(transpose_matrix(matrix), b)))
