def replacer(s, d):
    if d == '1':
        return s.replace('\t', '    ')
    elif d == '2':
        return s.replace('    ', '\t')
    else:
        print('Please enter 1 or 2')


src = input('Please choose the input source (s for string, f for file): ')
direction = input('Would you like to replace tabs with spaces (1) or spaces with tabs (2)? ')

if src == 's':
    str1 = input('Please enter a string: ')
    print(replacer(str1, direction))

elif src == 'f':
    filename = input('Please enter the file name: ')
    with open(filename, 'r') as file:
        data = file.read()
        data = replacer(data, direction)
    with open(filename, 'w') as file:
        file.write(data)
        print(data)
else:
    print('Please enter s or f')
