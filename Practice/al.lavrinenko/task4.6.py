matrix = [[0, 3, 0, 6],
          [7, 6, 8, 7],
          [0, 0, 3, 9]]

deletion = int(input("Enter the number to remove all columns containing it: "))

matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
matrix = [row for row in matrix if deletion not in row]
matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

print(matrix)
