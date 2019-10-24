"""
This module sorts numbers in the list (bubble sort).
"""

s = [0, 3, 0, 9, 2, 0, 1, 9]
# s = [4, 8, 5, 9, 5, 8, 6, 8, 84654, 84, 58, 84]

print(str(s))
for k in range(0,len(s)):
    for i in range(k,len(s)-1):
        if s[i+1] < s[i]:
            # a = s[i:i+2]
            # s[i:i+2] = a[::-1]
            # simplest substitution
            s[i], s[i + 1] = s[i + 1], s[i]

print(str(s))