def my_format(*args):
    length = len(args)-1
    template = args[0]
    for pos in reversed(range(len(template))):
        if template[pos] == '{' and template[pos+1] == '}':
            template = template[:pos]+args[length]+template[pos+2:]
            length -= 1
        elif template[pos] == '{' and template[pos+1] != '}':
            end = pos+1
            str_num = ""
            while template[end] != '}':
                str_num += template[end]
                end += 1
            number = int(str_num)
            template = template.replace(template[pos:end+1], args[number+1])
    return template


print(my_format('{1}, {0}, {2}', 'a', 'b', 'c'))
print(my_format('coordinates: {}, {}', '37.4N', '18.3W'))
print(my_format('{10}, {0}, {2}', 'a', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'u'))

