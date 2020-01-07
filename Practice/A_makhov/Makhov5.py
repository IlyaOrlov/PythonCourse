def func(a):
    for b, c in enumerate(a):
        b = b + 1
        d = "{} цифра равна {}".format(b, c)
        print(d)


func("10819")