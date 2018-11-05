matrix = [[45, 46, 78],
          [34, 22, 55],
          [48, 16, 89],
          ]
print(matrix)
matrix_t = list(zip(*matrix))
def fun(k):
	i=0
	for i in range(0, len(matrix_t)):
		if k in matrix_t[i]:
			del matrix_t[i]
			i +=1
fun(89)	
print (matrix_t)
result_matrix = list(zip(*matrix_t))
print (result_matrix)
    
