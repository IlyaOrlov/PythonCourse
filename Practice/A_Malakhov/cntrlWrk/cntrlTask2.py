def reverse1():
    l = [1, 2, 3, 4, 5]
    i = 0
    while i < len(l) / 2:
        l[i], l[len(l) - i - 1] = l[len(l) - i - 1], l[i]
        i += 1
    print(l)


reverse1()
