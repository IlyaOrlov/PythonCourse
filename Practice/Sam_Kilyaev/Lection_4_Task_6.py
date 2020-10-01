import random

len_of_matrix = int(input("Write len of matrix: "))
high_of_matrix = int(input("Write high of matrix: "))
your_number = int(input("Write number: "))


def make_matrix(len_of_matrix=3, high_of_matrix=5):
    A = [[0] * len_of_matrix for i in range(high_of_matrix)]

    for i in range(high_of_matrix):
        for j in range(len_of_matrix):
            A[i][j] = random.randint(0, 10)

    for i in A:
        print(f"{i}", end='')
        print()
    return A


def find_num_for_delete(matrix, num_delete):
    for i in matrix:
        for j in i:
            if j == num_delete:
                delete_column(i, j, matrix, num_delete)


def delete_column(i, j, matrix, num_delete):
    index = i.index(j)
    for a in matrix:
        del a[index]
    find_num_for_delete(matrix, num_delete)


def print_matrix(matrix):
    for i in matrix:
        print(f"{i}", end='')
        print()


arr = make_matrix(len_of_matrix, high_of_matrix)
matrix_test = [[1, 2, 2], [3, 4, 5]]
find_num_for_delete(matrix_test, 2)
print_matrix(matrix_test)
