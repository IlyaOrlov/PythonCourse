# Написать реализацию функции reversed функция принимает список,
# возвращает его же располагая элементы в обратном порядке 3 балла)


def my_reversed(t):
    if not isinstance(t, str):
        return  "Ошибка! Переданный объект не является строкой"
    return t[::-1]


def my_reversed1(t):
    if not isinstance(t, str):
        return  "Ошибка! Переданный объект не является строкой"
    res = ""
    for i in t:
        res=i+res
    return res

text = "123456789"
#a = my_reversed(text)
a = my_reversed1(text)
print(a)