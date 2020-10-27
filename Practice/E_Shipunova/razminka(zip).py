def trans_matrix(matrix):
    return [list(x) for x in zip(*matrix)]   # zip return an iterator of zip-obj


if __name__ == "__main__":
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]
    print(m)
    print(trans_matrix(m))
