def dict():
    dict = {}
    while True:
        a = input("input key")
        if a == "stop":
            break
        b = input("input value")
        dict[a] = b
    return dict

r = dict()
for str in open("222").readlines():
    print(str)
    prom = str.split()
    print
    for each in prom:
        str = str.replace(each, r.get(each))
print(str)
