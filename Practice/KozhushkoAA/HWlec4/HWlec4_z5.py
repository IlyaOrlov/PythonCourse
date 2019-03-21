d = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
s = 'Ready, set, 5, 4, 3, 2, 1, Go!'


def countdown(s):
    for key in d:
        s = s.replace(str(key), d[key])
    return s


print(countdown(s))