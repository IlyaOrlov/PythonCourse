def task2():
    n = int(input())
    m = int(input())
    if n < m:
        (n, m) = (m, n)
        return n
    else:
        return n


maxNum = task2()
print(maxNum)
