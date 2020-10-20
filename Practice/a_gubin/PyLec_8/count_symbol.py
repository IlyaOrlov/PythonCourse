def count_symbol(string, symbol):
    counter = 0
    for char in string:
        if char == symbol:
            counter += 1
    return counter


if __name__ == "__main__":
    a = "sd 2 fdf  2 dfsv"
    b = "gsdg 3 ssdg3 adfsf3"
    c = "5 sgdsd 5 sfd5 55 af"
    print(count_symbol(a, '2'))
    print(count_symbol(b, '3'))
    print(count_symbol(c, '5'))
