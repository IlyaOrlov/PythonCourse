#for Python 3.6
#lecture 5 task 1

def multiplier (m=1,source =[1,2,3]):
    result = source
    for i, x in enumerate(source):
        result[i] *= m
    return result
    
print("Старый метод:{}".format(multiplier(5)))
print("Старый метод:{}".format(multiplier(12, [1, 2])))

"""Ошибки: и переменная result, и переменная source ссылаются на один список,
который подвергается изменениям.
Переменная х, упомянутая в цикле, никак не используется."""

def my_multiplier (m=1,source =[1,2,3]):
    #Использует метод генерации списка
    return [x * m for x in source]


print("Новый метод:{}".format(my_multiplier(5)))
print("Новый метод:{}".format(my_multiplier(12, [1, 2])))

