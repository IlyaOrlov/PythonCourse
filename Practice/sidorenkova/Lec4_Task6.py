def del_col(mtx, num):
    col = []
    for i in range(len(mtx)):
        for j in range(len(mtx[i])):
            if mtx[i][j] == num and j not in col:
                col.append(j)

    col.sort()
    col.reverse()

    for i in range(len(mtx)):
        for x in col:
            del mtx[i][x]
    return mtx

def print_mtx(mtx):
    for i in range(len(mtx)):
        for j in range(len(mtx[i])):
            print(mtx[i][j], end='')
        print()


m = [[1, 1, 3, 4, 7, 10], [2, 0, 3], [3, 5, 7, 5]]
print_mtx(m)
print()
print_mtx(del_col(m, 3))