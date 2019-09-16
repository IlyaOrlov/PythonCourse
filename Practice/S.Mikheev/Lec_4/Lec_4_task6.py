n = int(input())  # количество строк матрицы
a = [[int(j) for j in input().split()] for i in range(n)]  # создаем матрицу из n строк
m = int(input())  # цифра, столбец с которой надо удалить
for i in reversed(range(n)):
    for j in reversed(range(len(a[i]))):
        if a[i][j] == m:
            for i in range(n):
                del (a[i][j])

for row in a:
    print(*row)