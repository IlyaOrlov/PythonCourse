text = 'Марка : brand; Модель : model; Цена : price'
t_r = {'brand':'Tesla', 'model':'Roadster', 'price':'19115775₽'}

for key in t_r.keys():
    text = text.replace(key, str(t_r[key]))

print(text)