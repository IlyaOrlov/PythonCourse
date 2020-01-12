def tab_on(text):
    text = text.replace("    ", "\t")
    return text

def tab_off(text):
    text = text.replace("\t", "    ")
    return text

file = open("mynewfile.txt", "w")
file.write("Snake\tgets\ttrapped\tin\tcar\tduring\tChristmas\tdrive")
file.close()

file = open("mynewfile.txt", "r+")
text1 = file.read()
res = tab_off(text1)
print(res)
file.close()

text2 = "A   snake   called   Allan   was   cut   free   from   a   car   by   firefighters"
res = tab_off(text2)
print(res)