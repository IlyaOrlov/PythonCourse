"""
This module reads integer number
and print each digit of the number in his own string.
"""

s = input('Enter integer number: ')
for k in range(0,len(s)):
    print(str(k+1) + ' цифра равна ' + s[k])