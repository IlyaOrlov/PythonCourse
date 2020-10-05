def replace(source, action):
    if source[-4] == '.' or source[-5] == '.':
        f = open(source, 'r')
        stroka = f.read()
        f.close()
        f = open(source, 'w')
        if action == "tab":
            f.write(stroka.replace('    ', '\t'))
        elif action == "space":
            f.write(stroka.replace('\t', '    '))
        else:
            return False
        f.close()
        return True
    else:  # string
        if action == "tab":
            return source.replace('    ', '\t')
        elif action == "space":
            return source.replace('\t', '    ')
        else:
            return None


print(replace("example.txt", "tab"))
