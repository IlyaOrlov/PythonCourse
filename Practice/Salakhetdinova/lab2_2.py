import random

a = int(random.randint(1, 50))
b = int(random.randint(1, 50))

def more(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    elif b == a:
        return None

print(more(a, b))  