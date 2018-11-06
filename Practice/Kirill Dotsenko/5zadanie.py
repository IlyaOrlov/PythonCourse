# 04.11 - [ИО]:  Проверено (есть замечания).
a=input("Which string:").lower()
b=input("Which word do u want to replace:").lower()
c=input("On what:").lower()
# 04.11 - [ИО]:  Шаблонов может быть несколько.
# Поэтому в словаре надо сохранять пары ключ:значение и затем,
# проходя по словарю, менять в строке "a" ключ из словаря "d"
# на соответствующее значение из словаря "d".
d={'k':c}
for v in d.values():
	print(a.replace(b,v).title())
