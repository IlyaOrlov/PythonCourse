def replacement(vvod, start, final):
    for strk in vvod:
        strk = strk.replace(start, final)
    return strk


a = open("111")
b = input("Что меняем ")
c = input("На что меняем ")
d = replacement(a, b, c)
print(d)
a.close()
