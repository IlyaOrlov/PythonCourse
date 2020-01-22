def interp(line, dic):
    for key in line.split():
        if key in dic:
            line = line.replace(key, dic[key])
    return line

l = "I have a p1\tI have an a1\tUgh a1 p1!"
d = {"p1": "pen", "a1": "apple"}

for each in interp(l, d).split(sep="\t"):
    print(each)
