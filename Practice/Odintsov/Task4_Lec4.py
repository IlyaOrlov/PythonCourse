x = input("Введите текст")

if "\t" in x:
    y = x.replace("\t", "    ")
elif "    " in x:
    y = x.replace("    ", "\t")

print(y)