def count_symbol(string, symbol):
    counter = 0
    for char in string:
        if char == symbol:
            counter += 1
    return counter


print(count_symbol("Hi, Elvis, I am here!", "e"))
