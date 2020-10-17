def del_column(_matrix, number):
    columns = {column for row in _matrix for column, digit in enumerate(row) if digit == number}
    columns = sorted(list(columns), reverse=True)
    return [[digit for index, digit in enumerate(row) if index not in columns] for row in _matrix]


matrix = [[1, 2, 3, 4, 5],
          [2, 5, 7, 3, 2],
          [9, 2, 3, 4, 8]]
for row in del_column(matrix, 3):
    print(row)
