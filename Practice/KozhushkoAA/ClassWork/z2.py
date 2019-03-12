s = [1, 77, 999, 777, 545, 888]


def revers(s):
    n = len(s) / 2
    i = 0
    j = len(s) - 1
    while i < n:
        s[i], s[j] = s[j], s[i]
        j -= 1
        i += 1
    return(s)


print(revers(s))