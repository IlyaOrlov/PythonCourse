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


arr = [[1, 2, 3, 4, 5],
       [1, 2, 7, 4, 5],
       [1, 2, 3, 7, 5],
       [1, 2, 3, 4, 5],
       [1, 2, 3, 4, 5]
      ]
delete_column(arr, 7)
