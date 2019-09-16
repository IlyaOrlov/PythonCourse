"""
This module delete a column in matrix
if this column contains the chosen number.
For tutorial purposes matrix is generated
as an array of random integer numbers.
"""

from random import randint as Random_integer
# random.randint(A, B) generates a random integer number N, A ? N ? B.

Ny = int(input('Please, enter number of rows: '))
Nx = int(input('Please, enter number of columns: '))

Rand_min = int(input('Let us define the range of your random numbers. '
                     'Enter minimual possible number: '))
Rand_max = int(input('Enter maximual possible number: '))

# Generation of random matrix
A = []
for i in range(0,Ny):
    Row = []
    for j in range(0,Nx):
        Element_ij = Random_integer(Rand_min, Rand_max)
        Row.append(Element_ij)
    A.append(Row)

if Nx and Ny < 7:
    print(str(A))  # Print matrix.

Fate = int(input('Enter the specific integer number '
                 'and I delete all rows that contain it. Your choice: '))

# Identification 'fatal' rows which contain the specific number.
Fatal_rows_indices = []
for i in range(0,Ny):
    Row_susp = A[i]
    print(str(Row_susp))
    for j in range(0,Nx):
        if Row_susp[j] == Fate:
            Fatal_rows_indices.append(j)

# print('Fatal Indices mess = ' + str(Fatal_rows_indices))  ## D&C
Fatal_rows_indices = set(Fatal_rows_indices)
Fatal_rows_indices = list(Fatal_rows_indices)
#print('Fatal Indices unique = ' + str(Fatal_rows_indices))  ## D&C

# Here we sort 'fatal' indices in (as in Task 3 for Lecture 4)
s = Fatal_rows_indices
for k in range(0,len(s)):
    for i in range(k,len(s)-1):
        if s[i+1] < s[i]:
            a = s[i:i+2]
            s[i:i+2] = a[::-1]

Fatal_rows_indices = s[::-1]
# print('Fatal Indices sorted = ' + str(Fatal_rows_indices))  ## D&C

# Delete a column in matrix if this column contains the chosen number
A_slim =[]
for i in range(0,Ny):
    Row = A[i]
    for k in Fatal_rows_indices:
        del Row[k]
    A_slim.append(Row)

for i in range(0,Ny):
    print(str(A_slim[i]))