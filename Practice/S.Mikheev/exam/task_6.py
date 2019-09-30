import re


def myformat(*args):
    k = args[0]
    n = len(args)
    for i in reversed(range(len(k))):
        if k[i] == '{' and k[i + 1] != '}':
            k = k.replace(k[i:i + 3], args[int(k[i + 1]) + 1])
        elif k[i] == '{' and k[i + 1] == '}':
            n -= 1
            # k = k.replace(k[i:i+2], args[n], 1)
            k = k[:i] + args[n] + k[i + 2:]
    return k


print(myformat('{1}, {0}, {2}', 'a', 'b', 'c'))
print(myformat('coordinates : {}, {}', '37.4N', '18.3W'))
line = '{1}, {0}, {2}'


# С Помощью регулярных выражений

def myformat2(*args):
    line = args[0]
    if re.search(r'[{][}]', line):
        for i in range(1, len(args)):
            line = re.sub(r'[{][}]', args[i], line, 1)
        return line
    if re.search(r'[{](\d)[}]', line):
        for elem in re.findall(r'[{](\d)[}]', line):
            line = re.sub(r'[{](\d)[}]', args[int(elem) + 1], line, 1)
        return line


print(myformat2('coordinates : {}, {}', '37.4N', '18.3W'))
print(myformat2('{1}, {0}, {2}', 'a', 'b', 'c'))
