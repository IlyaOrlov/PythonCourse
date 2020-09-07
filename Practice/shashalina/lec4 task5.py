# Task 4.4
# Интерполировать некие шаблоны в строке. Есть строка с определенного вида форматированием.
# # Необходимо заменить в этой строке все вхождения шаблонов на их значение из словаря.
#
#
# a = dict(one=1, two=2, three=3)

import re

def multiply(obj):

  number = re.findall('(\d+)', obj)
  str = "".join(number)
  print(str)
  obj.replace(str, str(int(str)*2))

  print (obj)


multiply("I have 1 cat")
