def replacingspace(str):
    return str.replace(" ", "\t")


def replacingtab(str):
    return str.replace("\t", "    ")


s = "слово слово слово слоао"
s = replacingspace(s)
print(s)
s = replacingtab(s)
print(s)