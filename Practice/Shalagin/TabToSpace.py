def changeStr(line,s1,s2):
    print(line)
    beg = line.find(s1)
    while not beg == -1:
        line = line[:beg] + s2 + line[beg + 1:]
        beg = line.find(s1)
        print(line)


line="keys:\tvalue:"
s1="\t"
s2="    "
changeStr(line,s1,s2)