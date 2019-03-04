x = float(input("Введите число:"))
l = [[1, 5, 8], [4, 7, 9], [0, 3, 2]]

for i in l:

    if x in i:
        a = i.index(x)
        for i in l:
            del i[a]

print(l)
