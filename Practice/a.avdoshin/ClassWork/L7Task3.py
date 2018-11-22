# 22.11 - [ИО]:  Проверено (есть замечания) - 0 баллов.
# не работает для my_range(1, 10, 2)
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
    # 22.11 - [ИО]:  это ж на каждой итерации разность вычисляется!
    while result[-1] != stop - step:
        result.append(start + step * count)
        count += 1
    return tuple(result)


print(my_range(10))
