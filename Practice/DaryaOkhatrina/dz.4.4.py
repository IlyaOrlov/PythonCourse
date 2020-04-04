s = '    roma    anna    '
def tab_func(s):
    s = s.replace('    ', '\t')
    return s
print(tab_func(s))


s1 = 'ann    roma    '
def space_func(s1):
    s1 = s1.replace('\t','    ')
    return s1
print(space_func(s1))

