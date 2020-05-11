a = input("Input number 1: ")
b = input("Input number 2: ")


def maximum(f, s):
    if int(a) > int(b):
        return a
    else:
        return b


print(maximum(a, b))
