import random

def printArray ( matrix ): 
   for i in matrix: 
      for j in i:
          print ( "{:4d}".format(j), end = "" ) 
      print ()
      
def deleteColumn(matrix, index):
    for i in matrix: 
            i.pop(index)

def deleteColumnByNumber(matrix, digit):
    for i in matrix: 
      for index, j in enumerate(i):
          if j == digit:
              deleteColumn(matrix, index)

if __name__ == '__main__':
    matrix = [[1,2,3,2,0],[4,5,6,1,5],[8,6,5,6,8],[3,5,0,8,2],[1,0,6,4,3]]
    printArray(matrix)
    print("input number for delete:")
    digit = int(input())
    deleteColumnByNumber(matrix, digit)
    printArray(matrix)