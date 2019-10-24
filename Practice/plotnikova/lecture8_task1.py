# 1. Написать реализацию встроенной функции len функция принимает
# список, возвращает его длину 3 балла)


def my_length(t):
    if not isinstance(t, list):
        return  "Ошибка! Переданный объект не является списком"
    res = 0
    for i in t:
        res+=1
    return res


text = ['1', '3', '4', '79', '78']
text1 = 1253
a = my_length(text)
print(a)
