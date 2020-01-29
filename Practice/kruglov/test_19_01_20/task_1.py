# 1 function MyLen
a = ["a", "b", "c", "d", "e"]


def MyLen(str_1):
    i = 0
    for el in str_1:
        i += 1
    return i


print(MyLen(a))
