arr = [0, 3, 24, 2, 3, 7]
def sortarray(n):
    for i in range(len(n) - 1):
        m = i
        b = i + 1
        while b < len(n):
            if n[b] < n[m]:
                m = b
            b = b + 1
        n[i], n[m] = n[m], n[i]

print(arr)
sortarray(arr)
print(arr)
