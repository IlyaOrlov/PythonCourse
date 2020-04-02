str = ('    roma    anna    ')
def tab_func(str):
    str = str.replace('    ', '\t')
    return str
print(tab_func(str))


str1 = ('ann    roma    ')
def space_func(str1):
    str1 = str1.replace('\t','    ')
    return str1
print(space_func(str1))
