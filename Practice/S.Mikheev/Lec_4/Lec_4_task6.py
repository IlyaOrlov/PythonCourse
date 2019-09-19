n = int(input())  # количество строк матрицы
a = [[int(j) for j in input().split()] for i in range(n)]  # создаем матрицу из n строк
m = int(input())  # цифра, столбец с которой надо удалить
k = []  # список индексом строк, в которых содержится цифра 'm'
for i in range(n):
    for j in range(len(a[i])):
        if a[i][j] == m:
            k.append(j)
k = sorted(set(k))
for elem in reversed(k):
    for i in range(len(a)):
        del a[i][elem]

for row in a:
    print(*row)
