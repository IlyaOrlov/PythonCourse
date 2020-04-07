text = 'Автомобиль разгоняется до 100 км/ч за время'
lst = text.split()
d = {'Автомобиль':'Audi', 'время':'5 секунд'}
for i in range(len(lst)):
     if lst[i] in d:
         lst[i] = d[lst[i]]
print(' '.join(lst))