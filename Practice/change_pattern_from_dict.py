def change():
    a='abc dfg abc'
    b = {'abc' : '1', 'dfg' : '2'}
    c = a.split(' ')
    for i, e in enumerate(c):
        if e in b:
            c[i] = b[e]
    c = ' ' .join(c)
    print(c)
change()

