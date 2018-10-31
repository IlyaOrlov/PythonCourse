import random
matrix = []
a = 10
for i in range(0, 10):
    line = []
    for j in range(0, 10):
        line.append(int(a - a*random.random()))
    matrix.append(line)
    print(line)
print('\n\n\n')
noNeedNum = 0 #int(input())
nums = set()
for i in matrix:
    for j in range(0, len(i)):
        if i[j] == noNeedNum:
            nums.add(j)
nums = list(nums)
nums.sort()
nums.reverse()

for i in nums:
    for j in matrix:
        del j[i]
for i in matrix:
    print(i)