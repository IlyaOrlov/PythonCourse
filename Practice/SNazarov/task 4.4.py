def tab_space(line, flag):
    if flag is True:
        array = line.split('\t')
        newLine = '    '.join(array)
        print(newLine)
    else:
        array = line.split('    ')
        newLine = '\t'.join(array)
        print(newLine)

tab = "Жил\tбыл\tпес!"
space = "Жил    был    пес!"
bool = True
print(tab)
tab_space(tab, bool)
bool = False
print(space)
tab_space(space, bool)

def file_spece_or_tab(line):
    array = line.split('    ')
    newLine = '\t'.join(array)
    print(newLine)

file = open('myfile.txt', 'r')
line = file.read()
file.close()

file_spece_or_tab(line)