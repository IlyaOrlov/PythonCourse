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
    for row in mtx:
        for each in x[::-1]:
            del row[each]
    return mtx


if __name__ == "__main__":
    matrix = [[0, 1, 0, 2, 3, 4], [1, 5, 6, 3, 0, 2], [7, 1, 9, 0, 1, 3]]
    element = 1
    print(del_find(element, matrix))
