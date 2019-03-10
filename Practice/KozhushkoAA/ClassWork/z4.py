a = input(str("Введите текст: "))


def to_title(a):
    a = a.split(" ")
    i = 0
    while i < len(a):
        a[i] = a[i].capitalize()
        i += 1
    n = ' '
    a = n.join(a)
    print(a)


to_title(a)