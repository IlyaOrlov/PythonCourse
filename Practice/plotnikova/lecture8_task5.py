# Написать функцию c ount_symbol считает сколько раз символ
# встречается в строке


def count_symbol(text, param):
    res=0
    for i in text:
        if i== param:
            res+=1
    return res


a=count_symbol ("111111a33333a4444a555a","a")
print(a)