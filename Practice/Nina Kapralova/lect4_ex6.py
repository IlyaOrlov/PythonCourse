def transpose(matr: list):
    res = []
    n = len(matr)
    m = len(matr[0])
    for j in range(m):
        tmp = []
        for i in range(n):
            tmp = tmp + [matr[i][j]]
        res = res+[tmp]
    return res


def del_column(matr: list, num: int):
    for line in matr:
        if num in line:
            matr.remove(line)
    return matr


# матрица для проверки
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
     ]


print(transpose(del_column(transpose(a), 5)))  # пример проверки функции