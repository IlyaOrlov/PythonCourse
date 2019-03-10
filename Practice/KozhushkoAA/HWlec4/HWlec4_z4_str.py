#c 4 пробелами на входе
a = 'Кожушко    Андрей    Андреевич'


def space_and_tab(a):
    a = list(a)
    i = 0
    while i < len(a):
        if a[i] == '\t':
            a[i] = '    '
        elif a[i:(i+4)] == [' ', ' ', ' ', ' ']:
            del a[(i+1):(i+4)]
            a[i] = '\t'
        i+= 1
    x = ''
    a = x.join(a)
    print(a)


space_and_tab(a)

#c табуляцией на входе
a = 'Кожушко\tАндрей\tАндреевич'


def space_and_tab(a):
    a = list(a)
    i = 0
    while i < len(a):
        if a[i] == '\t':
            a[i] = '    '
        elif a[i:(i+4)] == [' ', ' ', ' ', ' ']:
            del a[(i+1):(i+4)]
            a[i] = '\t'
        i+= 1
    x = ''
    a = x.join(a)
    print(a)


space_and_tab(a)