def to_title():
    a = 'qwerty asdfgh ssd dfg'
    b = a.split()
    i = 0
    while i < len(b):
        x = b[i]
        c = x.capitalize()
        i += 1
        print(c, end=' ')


to_title()
