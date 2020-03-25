def fun(*args):
    b = list(args)
    for n in b:
        i = 0
        m = i + 1
        if b[i] > b[m]:
            del b[m]
            m += 1
        else:
            del b[i]
            i += 1
            m += 1
    return b

print(fun(2, 7, 4, 3, 45, 1))