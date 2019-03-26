def count_symbol(str, symbol):
    z = 0
    for i in str:
        if i == symbol:
            z += 1
    print(z)

count_symbol("Hi, Elvis, I am here!", "i")