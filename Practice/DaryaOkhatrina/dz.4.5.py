s = 'cat is better than dog'
d = {'cat': 'кошка','dog': 'собака'}
for i in d:
    s = s.replace(i, (d[i]))
print(s)


s1 = s.split(' ')# преобразуем в список
for i in range(len(s1)):#проходим по списку с помощью цикла
    if i in d: # если элемент списка принадлежит словарю
        s1[i] = d[s1[i]]
print(' '.join(s1))# преобразуем обратно в строку

