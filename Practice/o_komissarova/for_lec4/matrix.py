def del_column(number, matrix):
    column_number = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == number:
                column_number.append(j)
    if column_number is None:
        print('number is not found')
    else:
        column_number.sort()
        column_number.reverse()
        for row in matrix:
            for number in column_number:
                del(row[number])
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for x in row:
            print("{:4d}".format(x), end="")
        print()


# delete two columns
matrix = [[1, 2, 3], [3, 5, 6], [7, 8, 9]]
print_matrix(matrix)
del_column(3, matrix)
print_matrix(matrix)

# delete all columns
matrix = [[1, 2, 3], [3, 5, 6], [7, 3, 9]]
print_matrix(matrix)
del_column(3, matrix)
print_matrix(matrix)


# delete one column
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_matrix(matrix)
del_column(3, matrix)
print_matrix(matrix)
