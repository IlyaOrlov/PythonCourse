def range(*num):
    if not all(isinstance(arg, int) for arg in num):
        raise TypeError('Только целые числа')
    start, step = 0, 1
    if len(num) == 1:
        result = num
    elif len(num) == 2:
        start, result = num
    elif len(num) == 3:
        start, result, step = num
        if step == 0:
            raise ValueError('Arg yне должно быть нулем')
    else:
        raise TypeError('Необходимо 3 arg')

    a = start
    if step > 0:
        while a < result:
            yield a
            a += step
    else:
        while a > result:
            yield a
            a += step


print(*range(2, 17, 2))
print(*range(-5, -15, -3))
