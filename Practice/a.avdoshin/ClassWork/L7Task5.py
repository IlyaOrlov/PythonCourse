def count_symbol(input_str, symbol):
    count = 0
    for i in range(len(input_str) - len(symbol)):
        if input_str[i:i + len(symbol)] == symbol:
            count += 1
    return count


print(count_symbol('Good by my friend, my only friend', 'my'))
