def my_format(*args):
    length = len(args)-1
    template = args[0]
    for pos in reversed(range(len(template))):
        if template[pos] == '{' and template[pos+1] == '}':
            template = template[:pos]+args[length]+template[pos+2:]
            length -= 1
        elif template[pos] == '{' and template[pos+1] != '}':
            template = template.replace(template[pos:pos+3], args[int(template[pos+1])+1])
    return template


print(my_format('{1}, {0}, {2}', 'a', 'b', 'c'))
print(my_format('coordinates: {}, {}', '37.4N', '18.3W'))

