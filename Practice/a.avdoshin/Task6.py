import random
matrix = []
for i in range(0, 10):
    line = []
    for j in range(0, 10):
        line.append(int(100 - 100*random.random()))
    matrix.append(line)
    print(line)
print('\n\n\n')
noNeedNum = 20 #int(input())
nums = []
for i in matrix:
    for j in i:
        if j == noNeedNum:
            nums.append(i.index(j))

for i in nums:
    for j in matrix:
        del j[i]
for i in matrix:
    print(i)