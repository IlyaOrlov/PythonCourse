def taborprob(stroka, cmd):
    if cmd == 1:
        return stroka.replace("\t", "    ")
    elif cmd == 2:
        return stroka.replace("    ", "\t")
    else:
        print("Введено неизвестное число")

stroka = input("Введите строку:")
cmd = int(input("1: tab->probel;\n2: probel->tab;\n"))
otvet = taborprob(stroka, cmd)
print("Измененная строка:", otvet)