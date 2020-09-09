def replace(source, action):
    if source[-4] == '.' or source[-5] == '.':
        f = open(source, 'r')
        str = f.read()
        f.close()
        f = open(source, 'w')
        if action == "tab":
            f.write(str.replace('    ', '\t'))
            f.close()
            return True
        elif action == "space":
            f.write(str.replace('\t', '    '))
            f.close()
            return True
        else:
            return False
    else:  # string
        if action == "tab":
            return source.replace('    ', '\t')
        elif action == "space":
            return source.replace('\t', '    ')
        else:
            return None


print(replace("example.txt", "tab"))
