import time

start = time.time()

with open('infile.txt') as fin:
    with open('outfile.txt', 'w') as fout:
        for line in fin:
            items = line.split()
            for each in items:
                if each.isdigit():
                    fout.write("{}, ".format(int(each)**2))

print("Total time: {}".format(time.time() - start))