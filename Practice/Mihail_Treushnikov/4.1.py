def change(source):
    if source[-4] == '.' or source[-5] == '.':
        f = open(source, 'r')
        string = f.read()
        f.close()
        f = open(source, 'w')
        if string.find('\t') != -1:
            f.write(string.replace('\t', '    '))
        else:
            f.write(string.replace('    ', '\t'))
        f.close()
    else:
        string = source
        if string.find('\t') != -1:
            return string.replace('\t', '    ')
        else:
            return string.replace('    ', '\t')


change("file.txt")
