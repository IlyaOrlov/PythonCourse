a = 'cat is better than dog'
b = {'cat': 'кошка','dog': 'собака'}
for i in b:
    a = a.replace(i, (b[i]))
print(a)


