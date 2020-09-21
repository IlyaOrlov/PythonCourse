
text = 'Какое плохое кафе. Обсллуживание не хорошее, Еда  не вкусная'
badrepgood = {'плохое': 'хорошее','не хорошее': 'хорошее','не вкусная': 'вкусная'}
print(text)
for i in badrepgood:
    text = text.replace(i, badrepgood[i])
print(text)