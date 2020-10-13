import random

a = int(random.randint(1, 50))
b = int(random.randint(1, 50))

def more(a, b):
    if a > b:
        print(f"{a} more {b}")
    elif b > a:
        print(f"{b} more {a}")
    elif b == a:
        print(f"{a} equal {b}")

more(a, b)