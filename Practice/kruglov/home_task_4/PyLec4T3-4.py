# 3
d = [0, 3, 24, 2, 3, 7]
b = []

i = 0
s = len(d)
while i < s:
    c = min(d)
    b.append(c)
    d.pop(d.index(c))
    i += 1

print(b)

# 3.1
g = [0, 3, 24, 2, 3, 7]

u = 0
while u < len(g):
    h = g.pop(g.index(min(g[u:]), u))
    g.insert(u, h)
    u += 1
print(g)

# 4

line = 'Ночь,\tулица,\tфонарь,\tаптека'
line2 = 'Ночь,    улица,    фонарь,    аптека'

line = line.replace('\t', '    ')
line2 = line2.replace('    ', '\t')

print(line)
print(line2)
