#Num 4
def to_title(s):
    s1 = s.title()
    print(s1)

s = 'dhhj df55 ghk 346'
to_title(s)

#Num 4/1
def to_title_1(s):
    s1 = s.split(' ')
    s2 = []
    for i in s1:
        i = i.title()
        s2.append(i)
    s2 = ' '.join(s2)
    return s2


s = 'dhhj df55 ghk 346'
print(to_title_1(s))

#Num 4/2
def to_title_1(s):
    s1 = s.split(' ')
    s2 = []
    for i in s1:
        s2.append(i[0].upper() + i[1:])
    s2 = ' '.join(s2)
    return s2

s = 'dhhj df55 ghk 346'
print(to_title_1(s))
