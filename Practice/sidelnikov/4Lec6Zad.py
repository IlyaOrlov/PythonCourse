def transport(matrix):
    if len(matrix) != 0:
        matrtran = [None]*len(matrix[0])

        for i in range(len(matrtran)):
            matrtran[i] =  [None]*len(matrix)

        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                matrtran[i][j] = matrix[j][i]
        return matrtran
    else:
        return matrix


def udalenie(mat):
    matrix = []
    for i in range(len(mat)):#строка
        if mat[i].count(chislo) == 0:
            matrix.append(mat[i])

    return matrix


matrix = [[8, 2, 1, 3, 6],
          [4, 2, 1, 1, 7],
          [7, 6, 7, 3, 1],
          [1, 1, 8, 6, 4]]
print("Матрица", matrix)
chislo = int(input("Введите число:"))
matrtran = transport(matrix)
matrix1 = udalenie(matrtran)
print("Транспонированнная матрица:", matrtran)
matrix2 = transport(matrix1)
print("Матрица без строк которые имеют число {}: ".format(chislo), matrix1)
print("Ответ:", matrix2)


