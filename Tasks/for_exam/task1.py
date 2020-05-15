lst = [3,3,2,5,5,5,4]

lst2 = sorted(list(set(lst)), key=lst.count)
print(lst2)