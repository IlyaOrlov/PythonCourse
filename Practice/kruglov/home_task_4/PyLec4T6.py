# 6 PyLecT6.py

def del_find(el, mtx):
    for row in mtx: 
        if el in row:
            x = row.index(el)
    for row in mtx: 
        row.remove(row[x])
    return mtx


if __name__ == "__main__":
    matrix = [[1,2,3], [4,5,6],[7,8,9]]
    element = 9
    del_find(element, matrix)
    print(matrix)