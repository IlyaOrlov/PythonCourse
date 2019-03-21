l = [4, 5, 0, 1, 9, 3, 7, 6, 8]

x = (len(l))/2
i = 0

while i < x:
    l[i], l[len(l)-i-1] = l[len(l)-i-1], l[i]
    i += 1

print(l)