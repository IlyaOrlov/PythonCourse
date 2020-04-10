def Replacement(vvod, new_file, start, final):
    for strk in vvod.readlines():
        strk = strk.replace(start, final)
        print(strk)
        new_file.write(strk)
    return new_file

with open("111") as work_file:
    b = input("Что меняем ")
    c = input("На что меняем ")
    with open("replaced", 'w') as new_file:
        Replacement(work_file, new_file, b, c)

