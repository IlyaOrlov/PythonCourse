#for Python 3.6
#task 6
matrix_example = [[23, 45, 61, 2, 7],
                  [7, 0, 789, 7, 2],
                  [61, 4, 13, 0, 13],
                  [15, 44, 11, 89, 2],
                  [2, 67, 85, 12, 55]]

def delete_column(matrix):
    '''Удаляет столбцы, содержащие указанное пользователем число'''
    num_to_del = int(input("Введите число, столбцы с которым вы хотите удалить\n"))
    index_list = []
    #Ищет, в каких строках под каким индексом находится заданное число, заносит индексы в список
    for line in matrix:
        if num_to_del in line:
            for i, number in enumerate(line):
                if number == num_to_del and i not in index_list:
                    index_list.append(i)
    print("Список удаляемых столбцов: {}".format([u+1 for u in sorted(index_list)]))
    #Удаляет столбцы в соответствии с индексами
    for j in sorted(index_list, reverse=True):
        for line in matrix:
            del line[j]
    return matrix
    
def main():
    for i in matrix_example:
        print(i)
    delete_column(matrix_example)
    for i in matrix_example:
        print(i)    



if __name__ == '__main__':
    main()

