def my_range(*args):
    for i in args:
        if not str(i).isdigit():
            try:
                float(str(i))
            except ValueError:
                return None
    start = 0
    step = 1
    stop = 0
    result = []
    if len(args) == 1:
        stop = args[0]
    elif len(args) >= 2:
        start = args[0]
        stop = args[1]
        if len(args) == 3:
            step = args[2]
            if step == 0:
                raise ValueError
    position = start
    if step > 0:
        while position <= stop:
            result.append(position)
            position += step
        return result
    else:
        while position >= stop:
            result.append(position)
            position += step
        return result


print(my_range(5))  # [0, 1, 2, 3, 4, 5]
print(my_range(2, 15))  # [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(my_range(2, 15, 2))  # [2, 4, 6, 8, 10, 12, 14]
print(my_range(15, 2, -2))  # print(my_range(15, 2, -2)) #
print(my_range(15, 2, "g"))  # None
