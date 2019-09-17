"""
This module sorts numbers in the list (selection sort).
"""

s = [9, 3, 0, 8, 2, 0, 1, 7]
# s = [4, 8, 5, 9, 5, 8, 6, 8, 84654, 84, 58, 84]

print(str(s))

sorted = []
for k in range(0,len(s)-1):
    s1 = s[k:]
    minimus = min(s1)
    index_min = s1.index(minimus)
    s[k], s[index_min+k] = s[index_min+k], s[k]

print(str(s))