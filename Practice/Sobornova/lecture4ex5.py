def key_change(a):
    for k in colors:
        a = a.replace(k, colors[k])
    return a


colors = {'1c': 'red', '2c': 'green', '3c': 'blue'}
e = key_change("1c 2c 3c")
print(e)
