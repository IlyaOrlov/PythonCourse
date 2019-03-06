s = [1, 1, 545, 888, 999, 777, 66, 1000, 888, 6, 8]


def revers(s):
    n = len(s) / 2
    i = 0
    j = len(s) - 1
    while i <= n:
        while j >= n:
            s[i], s[j] = s[j], s[i]
            j -= 1
            i += 1
        return(s)


print(revers(s))