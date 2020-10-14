def replacingspace(spacetab):
    return spacetab.replace("    ", "\t")

def replacingtab(spacetab):
    return spacetab.replace("\t", "    ")


s = "слово    слово    слово    слоао"
s = replacingspace(s)
print(s)
s = replacingtab(s)
print(s)
