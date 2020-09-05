def transpose(matrix):
    i_max = len(matrix)
    i = 0
    j_max = len(matrix[0])
    new_matrix = []
    for j in range(j_max):
        line = []
        while i < i_max:
            line.append(matrix[i][j])
            i += 1
        new_matrix.append(line)
        i = 0
    return new_matrix


def print_matrix(matrix):
    for row in matrix:
        for x in row:
            print("{:4d}".format(x), end="")
        print()


matr = [
    [1, 2, 3],
    [4, 5, 6]
]

print_matrix(matr)
print()
print_matrix(transpose(matr))
