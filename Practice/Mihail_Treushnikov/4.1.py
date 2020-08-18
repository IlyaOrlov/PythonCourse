def change (source):
    if (source[-4]=='.' or source[-5]=='.'):
        f = open(source, 'r')
        str = f.read()
        f.close()
        f = open(source, 'w')
        f.write(str.replace('    ','\t'))
        f.close()
    else:
        str = source
        return str.replace('    ','\t')

change("file.txt")

