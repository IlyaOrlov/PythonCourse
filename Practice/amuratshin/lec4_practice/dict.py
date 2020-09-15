d = {"cat": "кошка", "table": "стол"}

f = open("myfile.txt", "r")

for line in f:
    for k, v in d.items():
        line = line.replace(k, v)
        line = line.replace(k.capitalize(), v.capitalize())
    print(line)
