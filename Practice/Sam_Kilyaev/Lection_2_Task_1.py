import random

a = int(random.randint(1, 100))
b = int(random.randint(1, 100))


def more(a, b):
    if a > b:
        print(f"{a} more, than {b}")
    elif b > a:
        print(f"{b} more, than {a}")
    elif b == a:
        print(f"{a} equal {b}")


more(a, b)
