# 3 poor solution
# d = [0, 3, 24, 2, 3, 7]
# b = []

# i = 0
# s = len(d)
# while i < s:
#    c = min(d)
#    b.append(c)
#    d.pop(d.index(c))
#    i += 1

# print(b)

# 3.1
list1 = [0, 3, 24, 2, 3, 7]
el = 0
len_list = len(list1)
while el < len_list:
    min_ind = list1.index(min(list1[el:]), el)
    min_val = list1.pop(min_ind)
    if min_ind != el:
        zero_el = list1.pop(el)
        list1.insert(min_ind, zero_el)
    list1.insert(el, min_val)
    el += 1
print(list1)

# 4

line = 'Ночь,\tулица,\tфонарь,\tаптека'
line2 = 'Ночь,    улица,    фонарь,    аптека'

line = line.replace('\t', '    ')
line2 = line2.replace('    ', '\t')

print(line)
print(line2)
