# Task 4.4
# Интерполировать некие шаблоны в строке. Есть строка с определенного вида форматированием.
# Необходимо заменить в этой строке все вхождения шаблонов на их значение из словаря.
# a = dict(one=1, two=2, three=3)

def myReplace(obj):
  a  = {'one': 1, 'two': 2, 'three': 3}
  newStr = obj
  for key in a:
    if obj.find(key) > -1:
      newStr = newStr.replace(key, str(a[key]))

  return newStr

print (myReplace("I have one ... and two "))
