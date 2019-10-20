def count_symbol(text, symbol):
    count = 0
    for elem in text:
        if elem == symbol:
            count += 1
    return count


print(count_symbol("Hi, Elvis, I am here!", "i"))
