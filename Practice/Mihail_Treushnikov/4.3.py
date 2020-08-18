def del_matrix (matrix,number):
    i = 0
    j = 0
    while i<=len(matrix)-1:
        while j<=len(matrix[i])-1:
            if (matrix[i][j]==number):
                tmp = j
                j-=1
                for k in range(len(matrix)):
                    matrix[k].pop(tmp)
            j+=1
        i+=1
        j=0
    return matrix

def print_matrix(matrix):
    for row in matrix:
        for x in row:
            print("{:4d}".format(x), end="")
        print()

mat = [[1,4,7],[5,8,4],[1,1,1]]
print_matrix(mat)
del_matrix(mat,4)
print_matrix(mat)