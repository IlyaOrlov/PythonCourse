# 22.11 - [ИО]:  Проверено (ОК) - 3 балла из 3.
def my_len(lst):
    lenght = 0
    for i in lst:
        lenght += 1
    return lenght


test = [x for x in range(10)]
print(my_len(test), len(test))
