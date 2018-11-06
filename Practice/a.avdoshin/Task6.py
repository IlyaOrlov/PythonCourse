# 04.11 - [ИО]:  Проверено (есть замечания).
# 04.11 - [ИО]:  Добавляйте пустые строки после import и между логическими блоками кода
# 04.11 - [ИО]:  Решение должно быть оформлено в виде функции
import random
matrix = []
a = 10
# 04.11 - [ИО]:  Размер матрицы лучше занести в отдельную переменную,
# чтоб при необходимости поменять размер достаточно было бы сделать
# изменения в одном месте
for i in range(0, 10):
    line = []
    for j in range(0, 10):
        # 04.11 - [ИО]:  randint и randrange проще, изящней и быстрее.
        line.append(int(a - a*random.random()))
    matrix.append(line)
    print(line)
# 04.11 - [ИО]:  '\n'*3
print('\n\n\n')
noNeedNum = 0 #int(input())
nums = set()
for i in matrix:
    for j in range(0, len(i)):
        if i[j] == noNeedNum:
            nums.add(j)
nums = list(nums)
nums.sort()
# 04.11 - [ИО]:  nums.sort(reverse=True)
nums.reverse()

for i in nums:
    for j in matrix:
        del j[i]
for i in matrix:
    print(i)