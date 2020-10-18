def my_range(*args):
    start = 0
    stop = 0
    step = 1

    def condition():
        if step > 0:
            return start < stop
        else:
            return start > stop

    if len(args) == 3:
        start, stop, step = args
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 1:
        stop = args[0]
    else:
        print(f"Wrong number ({len(args)}) of arguments")
        raise TypeError
    if step < 0 and start < stop or step > 0 and start > stop:
        print("Incorrect interval")
        raise TypeError
    if step == 0:
        print("Incorrect step")
        raise TypeError
    res = []
    while condition():
        res.append(start)
        start += step
    return res


if __name__ == "__main__":
    print(my_range(20, 10, -2))
