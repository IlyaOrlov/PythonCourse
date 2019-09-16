"""
This module delete a column in matrix
if this column contains the chosen number.
For tutorial purposes matrix is generated
as an array of random integer numbers.
"""

from random import randint as random_integer
# random.randint(A, B) generates a random integer number N, A ? N ? B.

ny = int(input('Please, enter number of rows: '))
nx = int(input('Please, enter number of columns: '))

rand_min = int(input('Let us define the range of your random numbers. '
                     'Enter minimual possible number: '))
rand_max = int(input('Enter maximual possible number: '))

# Generation of random matrix
a = []
for i in range(0,ny):
    row = []
    for j in range(0,nx):
        element_ij = random_integer(rand_min, rand_max)
        row.append(element_ij)
    a.append(row)

if nx and ny < 7:
    print(str(a))  # Print matrix.

fate = int(input('Enter the specific integer number '
                 'and I delete all rows that contain it. Your choice: '))

# Identification 'fatal' rows which contain the specific number.
fatal_columns_indices = []
for i in range(0,ny):
    row_susp = a[i]
    print(str(row_susp))
    for j in range(0,nx):
        if row_susp[j] == fate:
            fatal_columns_indices.append(j)

# print('Fatal Indices mess = ' + str(fatal_columns_indices))  ## D&C
fatal_columns_indices = set(fatal_columns_indices)
fatal_columns_indices = list(fatal_columns_indices)
#print('Fatal Indices unique = ' + str(fatal_columns_indices))  ## D&C

# Here we sort 'fatal' indices in (as in Task 3 for Lecture 4)
s = fatal_columns_indices
for k in range(0,len(s)):
    for i in range(k,len(s)-1):
        if s[i+1] < s[i]:
            s[i], s[i + 1] = s[i + 1], s[i]  # Here I realize
            # the superiority of this method:
            # it does not need to declare new variable
            # and thus the possible conflict of variable names is avoided.

# Invert the order of indices to delete from the far end.
fatal_columns_indices = s[::-1]
# print('Fatal Indices sorted = ' + str(Fatal_rows_indices))  ## D&C

# Delete a column in matrix if this column contains the chosen number
a_slim =[]
for i in range(0,ny):
    row = a[i]
    for k in fatal_columns_indices:
        del row[k]
    a_slim.append(row)

for i in range(0,ny):
    print(str(a_slim[i]))