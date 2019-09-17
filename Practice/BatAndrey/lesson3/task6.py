matrix = [[2, 2, 3],
          [1, 1, 2],
          [3, 4, 5]]


def del_column(number):

    if matrix is number:
        count_for_del = matrix.count(number)
        for i in range(count_for_del):
            matrix[i].pop()
            print(matrix)
    else:
        print('we have not this number')

del_column(1)