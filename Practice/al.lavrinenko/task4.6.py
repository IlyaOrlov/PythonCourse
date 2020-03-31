array = [[0, 3, 0],
         [7, 6, 8],
         [0, 0, 3]]

deletion = int(input("Enter the number to remove all columns containing it: "))
columns_to_delete = []

for row in array:
    for column_index in range(len(row)):
        if row[column_index] == deletion and column_index not in columns_to_delete:
            columns_to_delete.append(column_index)

columns_to_delete.sort(reverse=True)

for row in array:
    for column_index in columns_to_delete:
        del row[column_index]

print(array)
