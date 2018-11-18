def ran(startstop, stop=None, step=1):
    start = 0
    if stop is not None:
        start = startstop
    else:
        stop = startstop
    # params validation
    if step is 0:
        print("Step must be more on less than 0")
        return
    if (stop - start) * step < 0:
        print("If step is less than 0, start must be more than stop, if more than 0 - start must be less")
        return
    a = list()
    a.append(start)
    i = 1
    if step > 0:
        while (start + i * step) < stop:
            a.append(start + i * step)
            i += 1
    else:
        while (start + i * step) > stop:
            a.append(start + i * step)
            i += 1
    return a


print(ran(20, 1, -0.5))
