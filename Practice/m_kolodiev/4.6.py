m = [
    [9, 4, 2, 3],
    [4, 5, 6, 2],
    [1, 4, 7, 8]
]

i = 2

m = zip(*m)
m = [row for row in m if i not in row]
m = zip(*m)
for row in m:
    print(row)
