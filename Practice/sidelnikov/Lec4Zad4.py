def taborprob(str, cmd):
    if cmd == 1:
        return str.replace("\t", "    ")
    elif cmd == 2:
        return str.replace("    ", "\t")
    else:
        print("Введено неизвестное число")

str = input("Введите строку:")
cmd = int(input("1: tab->probel;\n2: probel->tab;\n"))
otvet = taborprob(str, cmd)
print("Измененная строка:", otvet)