def Transport(matrix):
    MatrTran = [None]*len(matrix[0])

    for i in range(len(MatrTran)):
        MatrTran[i] =  [None]*len(matrix)

    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            MatrTran[i][j] = matrix[j][i]
    return MatrTran


def udalenie(MAT):
    matrix = []
    k = 0
    for i in range(len(MAT)):#строка
        if MAT[i].count(chislo) == 0:
            matrix.append(MAT[i])
            k += 1
    if k == 0:
        return 0
    else:
        return matrix


matrix = [[8, 2, 1, 3, 6],
          [4, 2, 1, 1, 7],
          [7, 6, 7, 3, 1],
          [1, 1, 8, 6, 4]]
chislo = int(input("Введите число:"))
MatrTran = Transport(matrix)
matrix1 = udalenie(MatrTran)
print("Матрица:", matrix)
print("Транспонированнная матрица:", MatrTran)
if matrix1 == 0:
    print("Ответ:", matrix1)
else:
    matrix2 = Transport(matrix1)
    print("Матрица без строк которые имеют число: ", matrix1)
    print("Ответ:", matrix2)


