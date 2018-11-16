def my_range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    assert step != 0
    if step > 0:
        assert stop > start
    else:
        assert stop < start
    result = [start]
    count = 1
    while result[-1] != stop - step:
        result.append(start + step * count)
        count += 1
    return tuple(result)


print(my_range(10))
