s = [5, 3, 36, 8, 0, 7, 0, 15]

a = 0

while a < len(s):
    s1 = s[a:]
    v = s1.index(min(s1))
    n = s.pop(v+a)
    s.insert(a, n)
    a += 1
else:
    print(s)