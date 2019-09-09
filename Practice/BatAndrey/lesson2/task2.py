def my_max(a, b):
    if b == 0:
        return a
    elif a // b > 0:
        return a
    else:
        return b


res = my_max(25, 8)
print('res =', res)