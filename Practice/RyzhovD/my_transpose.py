#! usr/bin/python3
## #! usr/bin/python3

"""
My version of matrix transpose
"""


from my_rand_matr_gen import my_rand_matr_gen

def my_transpose(matr):
    matr_tr = []

    if matr:  # condition check: empty matrix
        ny = len(matr)  # number of rows
        nx = len(matr[0])

        ##
        for i in range(0, ny):  # condition check: equal lengths of rows
            if len(matr[i]) != nx:
                print('The rows of your matrix are of nonequal lengths.')
                break

        ### Here the matrox transposition itself (6 lines + return)
        matr_tr = []
        for j in range(0, nx):
            row_j = []
            for i in range(0, ny):
                row_j.append(matr[i][j])
            matr_tr.append(row_j)

        return matr_tr

    else:
        return []


### TEST
a = my_rand_matr_gen(3, 4, 0, 9)
print('')
print('A = ')
for k in range(0,len(a)):
    print(a[k])

print('')
print('A^T = ')
a_tr = my_transpose(a)
for k in range(0,len(a_tr)):
    print(a_tr[k])

