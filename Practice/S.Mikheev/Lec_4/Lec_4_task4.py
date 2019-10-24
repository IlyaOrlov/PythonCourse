a = 'Hello!\n\t\tThis line was with two tabs\n\tThis line was with one tab\n'
print(a)
f = open('text.txt', 'w')
f.write(a)
f.close()

print(a.replace('\t', '    '))

with open('test.txt', 'r+') as f:
    for line in f:
        line.replace('\t', '    ')


