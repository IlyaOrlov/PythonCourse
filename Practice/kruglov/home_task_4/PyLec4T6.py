# 6 PyLecT6.py

def del_find(el, mtx):
    i = 0
    x = []
    for row in mtx: 
        while i < len(row):
            if el == row[i] and i not in x:
                x.append(i)
            i += 1
        i = 0
    x.sort()
    for row1 in mtx:
        cv = len(row)
        while i < cv:
            if row1[i] not in x:
                print(row1[i])
            # if row[z] not in x:
            #     print(row[el])
        # le = len(row)
        # while i < le:
            #if row[i] not in x[i]:
                # row.pop(0)
            i += 1
        #i = 0


if __name__ == "__main__":
    matrix = [[0,1,1], [0,5,6],[7,8,9]]
    element = 1
    del_find(element, matrix)
