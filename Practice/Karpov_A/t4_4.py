def spacesToTab(str):
    return str.replace(" ", "\t")


def tabToSpaces(str):
    return str.replace("\t", "    ")


s = "5 7 6 3"
s = spacesToTab(s)
print(s)
s = tabToSpaces(s)
print(s)