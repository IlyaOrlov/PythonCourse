#! usr/bin/python3

'''
Generation of a random integer matrix
PARAMETERS:
ny is a number of raws
nx is a number of columns
[rand_min, rand_max] is a range of a random integer
    (rand_min <= number >= rand_max)
'''

from random import randint as random_integer
# random.randint(A, B) generates a random integer number N,
# rand_min <= N >= rand_max.

# ny = int(input('Please, enter number of rows: '))
# nx = int(input('Please, enter number of columns: '))

# rand_min = int(input('Let us define the range of your random numbers. '
#                      'Enter minimual possible number: '))
#  rand_max = int(input('Enter maximual possible number: '))

def my_rand_matr_gen(ny, nx, rand_min, rand_max):
    a = []
    for i in range(0, ny):
        row = []
        for j in range(0, nx):
            element_ij = random_integer(rand_min, rand_max)
            row.append(element_ij)
        a.append(row)
    return a

### TEST
print(my_rand_matr_gen(3, 4, 0, 9))
