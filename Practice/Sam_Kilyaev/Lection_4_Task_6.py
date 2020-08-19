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


def delete_column(matrix, num_delete):
    index = None

    for i in matrix:
        for j in i:
            if j == num_delete:
                index = i.index(j)
                break
        if index is not None:
            break

    for i in matrix:
        del i[index]

    for i in matrix:
        print(f"{i}", end='')
        print()


arr = make_matrix(len_of_matrix, high_of_matrix)
delete_column(arr, your_number)
