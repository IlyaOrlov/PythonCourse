def count_symbol(string, symbol):
    frequency = 0
    for i in string:
        if i == symbol:
            frequency += 1
    return frequency


print(count_symbol('what  wonderful world', 'w'))
