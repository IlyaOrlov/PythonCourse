#Интерполяция строки str1
def fun(a,b):
    for i, j in b.items():
        a = a.replace(i, j)
    return a

#Исходная строка
text= "fdhhdudfijoihwpkwofnbgdgqknskbajdajdadoejernhfbd"
#Пример словаря
dict={'hh': '00', 'du': '22', 'df': '33',
      'ij': '44', 'oi': '55', 'hw': '66',
      'pk': '77', 'wo': '88', 'fn': '99',
      'bg': '10', 'dg': '12', 'qk': '13',
      'ns': '11', 'kb': '14', 'aj': '15',
      'da': '16', 'jd': '17', 'ad': '18','oe': '19'}

#запуск интерполяции
print("Новая строка: "+fun(text,dict))