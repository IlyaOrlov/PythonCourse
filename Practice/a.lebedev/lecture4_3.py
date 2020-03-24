a = (input('input your array:')).split()
i = 0
while i < len(a):
    index = 0
    minimum = min(a[i:])
    index = a[i:].index(minimum) + i
    a[index] = a[i]
    a[i] = minimum
    i += 1
print(a)
