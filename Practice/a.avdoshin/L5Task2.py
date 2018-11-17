def multiplier(m=1, source=[1, 2, 3]):
    for i in range(len(source)):  # Eе можно значительно упростить.
        source[i] *= m
    return source


print(multiplier(5, [2, 2, 3]))
