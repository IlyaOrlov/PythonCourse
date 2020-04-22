import time

ab_dict = {}

t = time.clock()
with open("infile.txt") as f:
    for line in f:
        info = line.split(' ')
        if info[0] in ab_dict:
            ab_dict[info[0]] += int(info[2])
        else:
            ab_dict[info[0]] = int(info[2])

with open("outfile.txt", "w") as f:
    for key, val in ab_dict.items():
        f.write(f"{key}: {val}\n")
print(time.clock() - t)
