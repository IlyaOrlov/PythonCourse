def my_range(*args):
    if not all(isinstance(arg, int) for arg in args):
        raise TypeError('All arguments must be integers')
    start, step = 0, 1
    if len(args) == 1:
        end = args
    elif len(args) == 2:
        start, end = args
    elif len(args) == 3:
        start, end, step = args
        if step == 0:
            raise ValueError('Arg 3 must not be zero')
    else:
        raise TypeError('Expected 1 to 3 arguments')

    num = start
    if step > 0:
        while num < end:
            yield num
            num += step
    else:
        while num > end:
            yield num
            num += step


print(*my_range(3, 10, 2))
print(*my_range(-8, -20, -3))
