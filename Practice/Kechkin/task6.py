# Есть список списков(матрица).Каждый внутренний список-это строка матрицы.
# Необходимо реализовать функцию,которая удаляет столбец,который содержит заданную цифру
import numpy


def matrix(num):
    m = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    index = numpy.argwhere(m == num)
    return numpy.delete(m, index, axis=1)


print(matrix(4))
