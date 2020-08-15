def replace(source, action):
    # check file or string
    formats = (".txt", ".json")
    type = None
    for i in formats:
        if i in source:
            type = "file"
    if type is None:
        type = "string"
    # work with file
    if type == "file":
        f = open(source, 'r')
        str = f.read()
        f.close()
        f = open(source, 'w')
        if action == "spaces_to_tabs":
            f.write(str.replace('    ', '\t'))
            f.close()
            return True
        elif action == "tabs_to_spaces":
            f.write(str.replace('\t', '    '))
            f.close()
            return True
        else:
            print("incorrect action. spaces_to_tabs or tabs_to_spaces are available")
            f.close()
            return False
    # work with string
    elif type == "string":
        if action == "spaces_to_tabs":
            return source.replace('    ', '\t')
        elif action == "tabs_to_spaces":
            return source.replace('\t', '    ')
        else:
            print("incorrect action. spaces_to_tabs or tabs_to_spaces are available")
            return None


print(replace("file.txt", "spaces_to_tabs"))
