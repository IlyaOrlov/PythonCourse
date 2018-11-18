def count_symbol(st, sym):
    if len(sym) is not 1:
        print("Lenght of symbol is more than 1")
        return
    #count of symbols
    cs = 0
    #count of letter
    cl = 0
    for i in range(0, len(st)):
        if st[i] == sym:
            cs += 1
        if st[i].lower() == sym.lower():
            cl += 1
    print("Count of symbols is {0}, count of letters - {1}".format(cs, cl))


count_symbol("Hi, Elvis, I am here!", "I")