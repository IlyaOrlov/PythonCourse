file = open("proba", "r+")
cmd = int(input("Введите число: 1 - табуляция -> "    "; 2 - "    " -> табуляция; :"))
if cmd == 1:
    for i in file:
        i.replace("\t", "    ")
    print(i)
elif cmd == 2:
    for i in file:
        i.replace("    ", "\t")
    print(i)
else:
    print("Говно")
file.close()

