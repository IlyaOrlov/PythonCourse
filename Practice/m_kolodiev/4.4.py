def spaces(string):
    return string.replace('    ', '\t')


def tabs(string):
    return string.replace('\t', '    ')


def file_spaces(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
        data = data.replace('    ', '\t')
    with open(file_name, 'w') as file:
        file.write(data)
        print(data)


def file_tabs(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
        data = data.replace('\t', '    ')
    with open(file_name, 'w') as file:
        file.write(data)
        print(data)


src = input('Please choose the input source (s for string, f for file): ')
direction = input('Would you like to replace tabs with spaces (1) or spaces with tabs (2)? ')
if src == 's':
    str1 = input('Please enter a string: ')
    if direction == '1':
        print(tabs(str1))
    elif direction == '2':
        print(spaces(str1))
    else:
        print('Please enter s or t')

elif src == 'f':
    filename = input('Please enter the file name: ')
    if direction == '1':
        file_tabs(filename)
    elif direction == '2':
        file_spaces(filename)
    else:
        print('Please enter 1 or 2')
