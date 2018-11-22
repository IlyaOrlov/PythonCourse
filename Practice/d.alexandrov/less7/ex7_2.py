def rev(a):
    l = len(a)
    for i in range(0, l//2):
        x = a[i]
        a[i] = a[l - i - 1]
        a[l - i - 1] = x
    return a


arr = [1, 4, 5, 6]
print(rev(arr))
