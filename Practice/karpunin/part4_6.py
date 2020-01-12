A = [[9, 2, 2], [4, 1, 0], [2, 7, 1]]
h = []

def fun(X):#Выводим массив
    for i in range(len(X)):
        for j in range(len(X[i])):
            print(X[i][j], end=' ')
        print()

fun(A)
p = int(input("Введите число, столбец с которым хотите удалить: "))

for i in range(len(A)):#определяем индексы искомых элементов
    for j in range(len(A[i])):
        if A[i][j] == p:
            h.append(j)
            #print("индекс   ", h)
h.sort(reverse=True)#обратная сортировка списка
#print(h)

for q in range(len(A)):#удаляем столбцы
    for x in h:
        del A[q][x]

fun(A)
