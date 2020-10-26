def my_len(seq):
    length = 0
    for _ in seq:
        length += 1
    return length


if __name__ == "__main__":
    print(my_len([1, 2, 3]))
    print(my_len({'a': 1, 'b': 2, 'c': 3, 'd': 4}))
    print(my_len({1, 2, 3}))
    print(my_len(range(10)))
