# 04.11 - [ИО]:  Проверено (ОК).
import random

import numpy as np


def benchmark(mult):
    def wrepper(*args, **kwargs):
        res = mult(*args, **kwargs)
        print(res)
        return res
    return wrepper

@benchmark
def mult(matrixX, matrixY):
    matrixX = np.array(matrixX)
    matrixY = np.array(matrixY)
    return matrixX.dot(matrixY)


def makeMatrix(sizeX=10, sizeY=10, dispersion=10):
    m = []
    for number in range(0, sizeY*sizeX):
        m.append(int(dispersion - random.random() * dispersion))
    m = np.array(m).reshape((sizeX, sizeY))
    return m


M1 = makeMatrix(5, 7)
M2 = makeMatrix(7, 3)
M3 = mult(M1, M2)
