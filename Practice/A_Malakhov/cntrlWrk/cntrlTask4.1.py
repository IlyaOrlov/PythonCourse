def to_title():
    a = 'sdsdd Asdd qwrrr'
    a = a.split()
    for x in range(len(a)):
        a[x] = a[x].capitalize()
    a = ' '.join(a)
    print(a)


to_title()
