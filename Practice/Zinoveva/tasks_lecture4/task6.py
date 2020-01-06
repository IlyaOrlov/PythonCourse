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
              return

if __name__ == '__main__':
    matrix = [[random.randint(0, 100) for j in range(5)] for i in range(5)]
    printArray(matrix)
    print("input number for delete:")
    digit = int(input())
    deleteColumnByNumber(matrix, digit)
    printArray(matrix)