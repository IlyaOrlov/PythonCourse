import math


print(3+5, '3'+'5')
print(2*3, '2'*3)
print(2 << 2)
print(11 >> 1)
print(5 & 3)
print(5 | 3)
print(5 ^ 3)
print(~5)
print(
    5 < 3,
    5 > 3,
    3 <= 6,
    4 >= 3,
    2 == 2,
    'str' == 'stR'
)

print(
    not 0,
    not False,
    0 and 1,
    True and False,
    0 or 1,
    True or False
)


x = y = [1, 2, 3, 'str']
x1 = [1, 2, 3, 'str']
y1 = [1, 2, 3, 'str']
one = 1
s = 'str'
print(
    x is y,
    x1 is y,
    x1 is y1,
    x is not y,
    y1 is not y,
    x1 is not y1,
    one in x,
    s in x,
    one in x1,
    s in y1,
)

print(int(5.98), round(5.98), round(5.98, 1))
