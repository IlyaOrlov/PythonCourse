inputfile = open('input.txt')
whatdoIdo = int(input())
outFile = open('out.txt', 'w')
for line in inputfile:
    if whatdoIdo == 0:
        outFile.write(line.replace('\t', '    '))
    else:
        outFile.write(line.replace('    ', '\t'))
        