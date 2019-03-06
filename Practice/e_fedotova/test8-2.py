def reversed(a):
    i = 0
    while i < len(a) / 2:
        a[i], a[len(a)-i-1] = a[len(a)-i-1], a[i]
        i += 1
    print(a)


a = [3, 6, 7, 0]
reversed(a)