def delete_column(list_of_lists, num_for_delete):
    print(list_of_lists)
    index = None  # for search index of num_for_delete

    for i in list_of_lists:         # 1. search index
        for j in i:
            if j == num_for_delete:
                index = i.index(j)
                print(index)        # take the first index with num_for_delete
                break
        if index != None:           # for exit from
            break

    for i in list_of_lists:         # 2. delete i[index]
        del i[index]

    print(list_of_lists)


def v2_delete_column(list_of_lists, num_for_delete):
    if len(list_of_lists) == 0:
        return None

    columns_for_del = []   # for indexes' columns for delete
    count = 0  # for editing an index

    for j in range(len(list_of_lists[0])):   # 1. search index for delete
        for i in range(len(list_of_lists)):
            if list_of_lists[i][j] == num_for_delete:
                columns_for_del.append(j)
                break

    for index in columns_for_del:  # 2. delete i[index]
        index -= count
        for i in list_of_lists:
            del i[index]
        count += 1

    return list_of_lists


arr = [[1, 2, 3, 4, 5],
       [2, 2, 7, 4, 5],
       [1, 2, 3, 7, 5],
       [1, 2, 3, 4, 5],
       [1, 2, 3, 4, 5]
      ]
delete_column(arr, 7)
print(v2_delete_column(arr, 7))
