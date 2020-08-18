def matrix(list, num, list_len):
    index = 0
    count = 0

    while count != list_len:
        count = 0

        for i in list:
            try:
                index = i.index(num)
            except ValueError:
                count += 1

        for j in list:
            del j[index]

    print(list)

num = 9
list = [[1, 2, 3, 4, 5],
        [1, 9, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 9, 5],
        [1, 2, 3, 4, 5]]
list_len = (len(list) - 1)
matrix(list, num, list_len)
