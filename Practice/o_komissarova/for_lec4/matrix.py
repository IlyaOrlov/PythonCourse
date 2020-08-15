def del_column(number, matrix):
    column_number = None
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == number:
                column_number = j
    if column_number is None:
        print('number is not found')
    else:
        for row in matrix:
            del(row[column_number])
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for x in row:
            print("{:4d}".format(x), end="")
        print()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_matrix(matrix)
del_column(9, matrix)
print_matrix(matrix)
