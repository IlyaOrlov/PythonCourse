import random


n, m = [int(i) for i in input('Введите через пробел размер матрицы: ').split(' ')]
matrix = [[random.randint(0, 9) for j in range(m)] for i in range(n)]
for row in matrix:
    print(row)
number = int(input('Столбец с какой цифрой удалить: '))

matrix = list(zip(*matrix))
matrix = [row for row in matrix if number not in row]
matrix = list(zip(*matrix))

for row in matrix:
    print(row)
