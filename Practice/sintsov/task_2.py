# 1
def print_max_from_two(a, b):
    if a > b:
        print(a)
    else:
        print(b)


# 2
def get_max_from_two(a, b):
    if a > b:
        return a
    return b


print_max_from_two(2,3)
print(get_max_from_two(4,5))