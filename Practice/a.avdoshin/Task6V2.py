import numpy as np
import random


def makeMatrix(sizeX=10, sizeY=10, dispersion=10):
    m = []
    for number in range(0, 100):
        m.append(int(dispersion - random.random() * dispersion))
    m = np.array(m).reshape((sizeX, sizeY))
    print(m, end='\n\n\n')
    return m


matrix = makeMatrix()
noNeedNumber = 0
matrix = matrix.T
nums = []
for i in range(0, len(matrix)):
    if noNeedNumber in matrix[i]:
        nums.append(i)

nums.reverse()

for i in nums:
    matrix = np.delete(matrix, i, 0)
matrix = matrix.T
print(matrix)
