a = 'home is better than flat'
b = {'home': 'дом','flat': 'квартира'}
for i in b:
    a = a.replace(i, (b[i]))

print(a)