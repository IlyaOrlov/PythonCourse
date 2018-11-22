def to_title(st):
    if st[0].islower():
        a = st[0].upper()
    else:
        a = st[0]
    for i in range(0, (len(st) - 1)):
        b = st[i+1]
        if st[i] is " ":
            b = b.upper()
        a += b
    print(a)

to_title('  orlov  Ilya evgenyevich')