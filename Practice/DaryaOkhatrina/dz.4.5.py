s = 'cat is better than dog'
d = {'cat': 'кошка','dog': 'собака'}
for i in d:
    s = s.replace(i, (d[i]))
print(s)

